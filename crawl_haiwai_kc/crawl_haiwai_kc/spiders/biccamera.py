import os
import scrapy
import time
from 万代监测库存.items import OutputItem
from 万代监测库存.items import HaiwaikcORM
from scrapy.http import Request
from 万代监测库存.tools.send import DingtalkMsgReport
import datetime


class BiccameraSpider(scrapy.Spider):
    name = 'biccamera'
    allowed_domains = ['biccamera.com']
    now = datetime.datetime.now()
    # log 文件夹不存在，就新建文件夹
    log_dirpath = os.path.join('.', 'log')
    if not os.path.exists(log_dirpath):
        os.makedirs(log_dirpath)

    # dev不更新 master 更新日志级别和保存路径
    custom_settings = {
        "LOG_FILE": os.path.join('.', 'log', '{name}_{timestp}.log'.format(name=name, timestp=now.strftime(r'%Y%m%d_%H%M%S'))),
        "LOG_LEVEL": 'INFO',
        'DB_TYPE': 'PG',
        'COOKIES_ENABLED': True,
        "ROBOTSTXT_OBEY": False,
        "ITEM_PIPELINES": {
            'crawl_haiwai_kc.pipelines.SqlalchemyPipeline': 300,
        },
        "SPIDER_MIDDLEWARES": {
            'crawl_haiwai_kc.middlewares.CrawlHaiwaiKcSpiderMiddleware': 543,
        },
        'HTTPERROR_ALLOWED_CODES': [301, 302],
        'REDIRECT_ENABLED': False,
    }

    def __init__(self, *args, **kwargs):
        self.logger.debug('Spider:%s className: %s, function: %s' %
                          (self.name, self.__class__.__name__, '__init__'))
        super(BiccameraSpider, self).__init__(*args, **kwargs)
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
        spider = super(BiccameraSpider, cls).from_crawler(
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

    def get_item_get(self, paramas=None, callback=None):
        payload = {}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }

        url = paramas['goods_url']

        meta = {
            "paramas": paramas,
        }
        # return Request(url=url, callback=callback, headers=headers, meta=meta, dont_filter=True)
        return Request(url=url, callback=callback, headers=headers, meta=meta)

    def parse(self, response):
        paramas = response.meta['paramas']
        item = OutputItem()
        # # 商品名称
        goods_name = response.xpath('//h1[@id="PROD-CURRENT-NAME"]/text()').extract_first()
        item["goods_name"] = goods_name or None
        item["goods_id"] = paramas["goods_id"]
        item["goods_url"] = response.url
        item["thedate"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        icon = response.xpath('//tr[@class="bcs_variationOff"]/td[@class="bcs_stock"]/p/span/text()').extract_first()

        if not icon:
            item["goods_status"] = -1  # 未知错误
        elif icon == '在庫あり':
            item["goods_status"] = 1  # 有库存
        else:
            item["goods_status"] = 0  # 无库存

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
                                        num=i + 1, except_message=self.exception_message.pop())

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

            title_content = '{platform}平台,总处理: ***{total}***, 变化: ***{exchange}***, 无效: ***{invalid}***'.format(
                platform=self.name,
                total=self.total_len, exchange=self.exchage_num, invalid=self.invalid_num)

            content = '### {title_content}\n{cachemessage}\n{at_content}'.format(title_content=title_content,
                                                                                 at_content=at_content,
                                                                                 cachemessage=self.cache_message)

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

