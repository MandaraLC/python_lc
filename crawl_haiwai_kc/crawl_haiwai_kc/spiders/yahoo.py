import scrapy
import time
from 万代监测库存.items import OutputItem
from 万代监测库存.items import HaiwaikcORM
from scrapy.http import Request
from 万代监测库存.tools.send import DingtalkMsgReport
import datetime
import os


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['store.shopping.yahoo.co.jp']
    start_urls = []
    now = datetime.datetime.now()
    custom_settings = {
        # "LOG_FILE": os.path.join(
        #    '.', 'log', '{name}_{timestp}.log'.format(name=name, timestp=now.strftime(r'%Y%m%d_%H%M%S'))),
        # "LOG_LEVEL": 'INFO',
        "ROBOTSTXT_OBEY": False,
        "ITEM_PIPELINES": {
            'crawl_haiwai_kc.pipelines.SqlalchemyPipeline': 300,
        },
        "SPIDER_MIDDLEWARES": {
            'crawl_haiwai_kc.middlewares.CrawlHaiwaiKcSpiderMiddleware': 543,
        },
        # "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        "DOWNLOADER_MIDDLEWARES": {
            'crawl_haiwai_kc.middlewares.RandomUserAgentDownloaderMiddleware': 543,
        },
    }
    handle_httpstatus_list = [404]

    def __init__(self, *args, **kwargs):
        self.logger.debug('Spider:%s className: %s, function: %s' %
                          (self.name, self.__class__.__name__, '__init__'))
        super(YahooSpider, self).__init__(*args, **kwargs)
        """
        获取命令行参数
        """
        # 加载必要参数
        self.mode = kwargs.get('mode', 'DEV')  # str
        self.frequency_min = kwargs.get('freq_min', 23)

        # 初始参数
        self.cache_message = ''
        self.total_len = 0
        self.exchage_num = 0
        self.invalid_num = 0
        self.exception_message = set()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(YahooSpider, cls).from_crawler(
            crawler, *args, **kwargs)
        spider.logger.debug('Spider:%s className: %s, function: %s' % (
            spider.name, spider.__class__.__name__, 'from_crawler'))
        crawler.signals.connect(spider.spider_opened,
                                scrapy.signals.spider_opened)
        return spider

    def start_requests(self):
        self.logger.debug('Spider:%s className: %s, function: %s' % (
            self.name, self.__class__.__name__, 'start_requests'))
        res = self.sqlalchemy_spider_session.query(
            HaiwaikcORM).filter(HaiwaikcORM.platform == self.name, HaiwaikcORM.frequency == self.frequency_min)
        self.total_len = len(res.all())
        for val in res:
            paramas = {
                'goods_url': val.url,
                "goods_id": val.id,
            }
            yield self.get_item_get(paramas=paramas.copy(), callback=self.parse)
            # yield scrapy.Request(
            #     url=val[1],
            #     callback=self.parse,
            #     meta={
            #         "goods_id": val[0],
            #         "goods_url": val[1]
            #     }
            # )

    def get_item_get(self, paramas=None, callback=None):
        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }

        url = paramas['goods_url']

        meta = {
            # "proxy": "https://127.0.0.1:8888",
            "paramas": paramas,
        }
        return Request(url=url, callback=callback, headers=headers, meta=meta)

    def parse(self, response):
        paramas = response.meta['paramas']
        item = OutputItem()
        # # 商品名称
        item["goods_name"] = response.css(
            '.mdItemName p.elName::text').extract_first()
        item["goods_id"] = paramas["goods_id"]
        item["goods_url"] = paramas["goods_url"]
        item["thedate"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 如果url返回是404就是链接失效了，需要通知管理人更改url
        if response.status == 404:
            item["goods_status"] = -1
            yield item
        else:
            # yahoo平台 商家自定义文字，不好判断。
            # 有货 <button class="elButton isReservation" data-ylk="slk:reserve;pos:0;" id="add_cart">\n        <span>予約注文する</span>\n    </button>
            # 按钮状态
            # css 获取指定标签的上的属性
            btnStatus = response.css(
                '#cart_button>button::attr(class)').extract()
            # # 按钮文字 失效，有可能没有库存的商品，文字还是予約注文する
            # btnText = response.css(
            #     '#cart_button>button>span::text').extract_first() or ""
            # 商品数量
            selectDom = response.css(
                '.mdQuantityCounter select option::text').extract_first()
            # """ fail
            #     判断库存方法：
            #     1、判断按钮的文字
            #         予約注文する ---- 有库存
            #         商品をカートに入れる ---- 没有库存
            #     2、判断商品数量选择按钮是否存在
            #         商品数量大于0则是有库存，等于0则是无库存
            #     3、以上都不符合则返回-1
            # """
            """ 
                判断库存方法：
                1、按钮属性
                    isDisabled ---- 无货
                    not isDisabled ---- 有库存
                2、判断商品数量选择按钮是否存在
                    商品数量大于0则是有库存，等于0则是无库存
                3、以上都不符合则返回-1
            """
            if 'isDisabled' in btnStatus:
                item["goods_status"] = 0  # 无库存
                pass
            elif not selectDom:
                item["goods_status"] = 0  # 无库存
            elif int(selectDom) > 0:
                item["goods_status"] = 1  # 有库存
            else:
                item["goods_status"] = -1  # 未知错误

            # if btnText == '予約注文する':
            #     item["goods_status"] = 1  # 有库存
            # elif btnText == '商品をカートに入れる':
            #     item["goods_status"] = 0  # 无库存
            # else:
            #     item["goods_status"] = -1  # 未知错误
            yield item

    def spider_opened(self, spider):
        self.logger.debug('Spider:%s className: %s, function: %s' %
                          (self.name, self.__class__.__name__, 'spider_opened'))
        # 创建 一个指定的 Session 类实例
        self.sqlalchemy_spider_session = self.crawler.spider.db_SessionFactory()
        self.logger.debug('init sqlalchemy_spider_session,id is {}'.format(
            id(self.sqlalchemy_spider_session)))

    def closed(self, reason):
        self.logger.debug('Spider:%s className: %s, function: %s' %
                          (self.name, self.__class__.__name__, 'closed'))

        # 获取spider stats
        # self.crawler.stats.get_stats()
        # self.crawler.stats.get_value('log_count/ERROR')

        # 关闭spider 打开的链接
        self.sqlalchemy_spider_session.close()
        self.logger.info('close sqlalchemy_spider_session')

        if self.exception_message:
            self.logger.debug('Spider:%s 通知开发者' % (self.name))
            report = DingtalkMsgReport(webhook=self.settings.get('%s_CONFIG' % self.mode)[
                                       'DINGTALK_DEVER_WEBHOOK'], secret=self.settings.get('%s_CONFIG' % self.mode)[
                                       'DINGTALK_DEVER_SECRET'])

            at_who_mobiles = ['']
            at_who_mobiles = at_who_mobiles + self.settings.get('%s_CONFIG' % self.mode)[
                'DEVER_AT_MOBILES']
            at_content = '@'.join(at_who_mobiles)
            exception_message = ''
            for i in range(len(self.exception_message)):
                exception_message = exception_message + \
                    '> {num}、 {except_message} \n\n'.format(
                        num=i+1, except_message=self.exception_message.pop())

            content = '### {platform} ERROR\n{cachemessage}\n\n{at_content}'.format(
                platform=self.name, at_content=at_content, cachemessage=exception_message)

            report.chatbot_makedown(title='{platform} 消息通知'.format(
                platform=self.name), content=content, atMobiles=at_who_mobiles[1:])

        if self.cache_message:
            self.logger.debug('Spider:%s 通知业务者' % (self.name))
            # 含有信息，通知业务部门
            report = DingtalkMsgReport(webhook=self.settings.get('%s_CONFIG' % self.mode)[
                                       'DINGTALK_BIS_WEBHOOK'], secret=self.settings.get('%s_CONFIG' % self.mode)[
                                       'DINGTALK_BIS_SECRET'])

            at_who_mobiles = ['']
            at_who_mobiles = at_who_mobiles + self.settings.get('%s_CONFIG' % self.mode)[
                'BIS_AT_MOBILES']
            # at_who_mobiles.append(
            at_content = '@'.join(at_who_mobiles)

            title_content = '{platform}平台,总处理: ***{total}***, 变化: ***{exchange}***, 无效: ***{invalid}***'.format(platform=self.name,
                                                                                                                total=self.total_len, exchange=self.exchage_num, invalid=self.invalid_num)

            content = '### {title_content}\n{cachemessage}\n{at_content}'.format(title_content=title_content,
                                                                                 at_content=at_content, cachemessage=self.cache_message)

            result = report.chatbot_makedown(title='{platform}平台侦察'.format(
                platform=self.name), content=content, atMobiles=at_who_mobiles[1:])
            if result.status_code == 200:
                self.logger.info('{title_content},已通知业务者'.format(
                    title_content=title_content))

            else:
                message = 'url:{url}, status_code:{status_code},reason:{reason},text:{text}'.format(
                    url=result.url, status_code=result.status_code, reason=result.rereasonson, text=result.text)
                self.logger.error('{title_content},未能通知业务者！！！！！！！ message:{message}'.format(
                    title_content=title_content, message=message))
