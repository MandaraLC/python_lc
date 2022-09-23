import scrapy
import time
from 万代监测库存.items import OutputItem
from 万代监测库存.items import HaiwaikcORM
# from crawl_haiwai_kc.mysqlConnector import Mysql
from scrapy.http import Request
from 万代监测库存.tools.send import DingtalkMsgReport
import datetime
import os


class YodobashiSpider(scrapy.Spider):
    name = 'yodobashi'
    allowed_domains = ['www.yodobashi.com']
    start_urls = []
    now = datetime.datetime.now()
    custom_settings = {
        # "LOG_FILE": os.path.join(
        #    '.', 'log', '{name}_{timestp}.log'.format(name=name, timestp=now.strftime(r'%Y%m%d_%H%M%S'))),
        # "LOG_LEVEL": 'INFO',
        "ROBOTSTXT_OBEY": False,
        "CONCURRENT_REQUESTS": 3,
        "ITEM_PIPELINES": {
            'crawl_haiwai_kc.pipelines.SqlalchemyPipeline': 300,
        },
        "SPIDER_MIDDLEWARES": {
            'crawl_haiwai_kc.middlewares.CrawlHaiwaiKcSpiderMiddleware': 543,
        },

        # "DOWNLOADER_MIDDLEWARES": {
        #     'crawl_haiwai_kc.middlewares.RandomUserAgentDownloaderMiddleware': 200,
        # },
        # "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

    def __init__(self, *args, **kwargs):
        self.logger.debug('Spider:%s className: %s, function: %s' %
                          (self.name, self.__class__.__name__, '__init__'))
        super(YodobashiSpider, self).__init__(*args, **kwargs)
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
        spider = super(YodobashiSpider, cls).from_crawler(
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
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'yuid=C6051D8A8A1EC53121970FFF6214A3F4; yid=C6051D8A8A1EC53121970FFF6214A3F4; newses=1; uq=bd11f8159d4d204c3f6e4461c51c31bddfe9a700; yatpz=C1A0S%2FvYjh59mGSJ4Sk%2BoqFlwQ%3D%3D; JSESSIONID=02AE4A18EAF63F286171BCFAA14AADB1; hty_logout_time="100000001006105282-1620616877282:"; bm_sz=87D38E00CB58C31D3994CDBE81D6ACF5~YAAQTENKy2NlxTR5AQAA9hdLVAsp7Vmry2CWyT7oNUpN/W340KYDOXPm7+m2+ldqkQY3Pg0G4jq6TbEuK/xRQcDtY24UcfoiojOgtyrm4W4YZen+56WVFsOK6ZrBu4+uo/Fgn3fibEN5zDuFaBnSDias9r+yCrS1vZTUfZwIwpS2AljYwoZOzF5TVJQLstEsgzc=; RT="z=1&dm=yodobashi.com&si=dxx4evgsyj5&ss=koi1g2zt&sl=0&tt=0"; _abck=F112F354DCE9196B878C7A890B01AA98~0~YAAQTENKy2dlxTR5AQAAdB9LVAVSR5inigup6V8wg5oF1t//Mu52rp9sWRtE1vqygF1YgSSujLBridonirvMu+rt89nv562xFjypROsfXshojLXFC4FkhCMcVQUJiZ3zq7WrJbu781KfCmYYksRtTiYyx0SbKFC8M4Z5N/ElHoq3N1u1dStFbNaV1XhmUax8JMrgPPN2XUQpREPTAXlA51CY3HkgZBZnHQoCEwzVNYHUpiHa94ZZO+FAQlkKD2JQkp2fME+ielPf4spqWeSadPSAQsUJWxuL++vE8tEQKcOB2JkMb32dbbxtIzaJ0umtJviYR1bnmXegmiXb22ekFMimXmQ8cNyHYG1Q5EHWiEeHyiS+InV4HlSpCBD6EFYbyyi79Mc8t/O+ueMIVVaVu/ReKCN4DgAWN5jI~-1~-1~-1; ak_bmsc=49B14DE406D8405CCD7BA93B71C2CA72CB4A434CFD180000AEA69860B8E88659~plX5gT/nIdVjPb7UIxa1p6OK4ud5JGL7jSv26MePMm+GZfDEr2ueBgLdl2s7aCPiHNkA2WdWRbA1Fff1HS7Xry4ZN5XWjSsIvG3eH43B1iVsJ1SHMPxorFrtkPnvGn1ijHP8CPmaujRjfTREnhC6kKChQkx/PGGJPi0tBPiPOXX1EblNIeVUC5caTZYelsrah2A9zzGXFZEcVPUjMYA4GiulIKAqnOVObIoD5AaK3z6/3JkoDXbWHe85+HabL34vsE; dduif=",,1,bz8PfNRS9ujVJc1eSq0vF4VSkPvNgeut,1"; bm_sv=C075DD16E4823A8325C337E59B3C7A34~z4KHEsKiQS4sEryobUrATlCPZ7P794P4gydCj/wdcfIxr10S69IyjVuOHfBREeKYUYiN32glvAe1sSJOOVYrd03ym6k/ToCmefjA4yJaRnMWEuTviJkKuzItRnF3tovtzKC17MzCluoeAo6jrY0kt49x0yI2CYCCCAmnYftEhJo=; __ukwlgck=9894717.1388767992.0_1_154810416.1620616881594_154810416.688175266.1620616881594; _ts_yjad=1620616882132; _gcl_au=1.1.397066931.1620616882; _ga=GA1.2.1861885630.1620616883; _gid=GA1.2.661382283.1620616883; _dc_gtm_UA-34284167-1=1; newses=0; uq=65a7963e00891fa4a83093c28f596cca12d363c1; JSESSIONID=8EABC7C47567300CD39D66988AD970A6; hty_logout_time="100000001006105282-1620616908164:"; bm_sv=C075DD16E4823A8325C337E59B3C7A34~z4KHEsKiQS4sEryobUrATlCPZ7P794P4gydCj/wdcfIxr10S69IyjVuOHfBREeKYUYiN32glvAe1sSJOOVYrd03ym6k/ToCmefjA4yJaRnNoITZq+hR9ixu2rBqBu5FMdjQz16R+7f+E3Ruk3ne37/54eFLRgYX/z9UpmjVRQB8=; _abck=F112F354DCE9196B878C7A890B01AA98~-1~YAAQTiLHF3SVxFF5AQAAMI9LVAUCb9ddXC9K772pZcD09g/DSRxvnaxW7ThK3B0p7tpDpfmN9rgCBXu+ZxfgYt4cxq6oH6niDbb7auQHDvcrBV3da1hUAiRnF083DV6XVEx8RBAk2Hc8hiSPAzOZ/ee+G5SZc0ntfDcrvZ16HRL1t6hY3qcU94/lwj3TNkjWIN1iM8YucGkPA747j6dHFjEkmKPqGjuSfHbDN3bhklZXcEVcyZOjIdqhDk2o6Sq6n2uIVIy/mZ5rycb4SynQ5Mm6ykz+mu1tFkP6DYn3OrgUjXPgpC3IOnz6GBIrP7BT4/ARALGT8vGk0MIiAP4MTaRFiEt7PEL/ce7g8N88zg1/1LytrAL2b2XOWl5yEuwN3XUSyYmBARNeR9L7+qtMUISN9ZGvKbXA/F4j~0~-1~-1',
            'Host': 'www.yodobashi.com',
            'Pragma': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }

        url = paramas['goods_url']

        meta = {
            # "proxy": "https://127.0.0.1:8888",
            "paramas": paramas,
        }
        return Request(url=url, callback=callback, headers=headers, meta=meta)

    def parse(self, response):
        paramas = response.meta['paramas']
        # print("-------------------Yodobashi start---------------------")
        item = OutputItem()
        # 商品名称
        goods_name = response.css(
            '#products_maintitle span[itemprop="name"]::text').extract_first()
        # 购买按钮
        sub_btn = response.css('#js_m_submitRelated').extract_first()
        # 没有库存
        sold_out = response.css(
            '#js_buyBoxMain .salesInfo p::text').extract_first()

        item["goods_name"] = goods_name
        item["goods_id"] = paramas["goods_id"]
        item["goods_url"] = paramas["goods_url"]
        item["thedate"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        """ 
            判断库存方法：
            1、判断是否有购买按钮 --- 有则有库存
            2、判断是否有没库存的标签 --- 有标签则是没有库存
            3、以上都不符合则返回-1
        """
        # 判断是否可购买
        if sub_btn:
            item["goods_status"] = 1  # 有库存
        elif sold_out:
            item["goods_status"] = 0  # 无库存
        else:
            item["goods_status"] = -1  # 未知错误

        yield item
        # print("-------------------Yodobashi end---------------------")

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
