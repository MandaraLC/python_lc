# -*- coding: utf-8 -*-
"""

"""
import json
import os
import scrapy
import time
import re
from crawl_haiwai_kc.items import OutputItem
from crawl_haiwai_kc.items import HaiwaikcORM
from scrapy.http import Request
from crawl_haiwai_kc.tools.send import DingtalkMsgReport
import datetime
import requests
import random


class BandaiSpider(scrapy.Spider):
    name = 'bandai'
    allowed_domains = ['p-bandai.jp']
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
        'REDIRECT_ENABLED': True,
    }

    def __init__(self, *args, **kwargs):
        self.logger.debug('Spider:%s className: %s, function: %s' %
                          (self.name, self.__class__.__name__, '__init__'))
        super(BandaiSpider, self).__init__(*args, **kwargs)
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
        #代理
        self.proxy = self.ipadea_proxy()

    #代理
    def ipadea_proxy(self):
        # 代理api
        proxy_url = 'http://api.proxy.ipidea.io/getProxyIp?num=1&return_type=json&lb=1&sb=0&flow=1&regions=jp&protocol=http'
        ipport = []
        for i in range(5):
            # 加代理
            try:
                respone = requests.get(proxy_url)
                json0 = json.loads(respone.text)
                if json0['code'] == 0:
                    ipport = json0['data'][0]
            except:
                pass
            if ipport:
                break
        # 不加代理
        return ipport

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BandaiSpider, cls).from_crawler(
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
                # "cookies": '_TSTD=a%3A2%3A%7Bs%3A7%3A%22TraceId%22%3Bs%3A32%3A%224410e2c8408562a1ddc419dc2ea9b569%22%3Bs%3A7%3A%22setTime%22%3Bi%3A1627886486%3B%7D; _TSD=a%3A2%3A%7Bs%3A9%3A%22SessionId%22%3Bs%3A34%3A%22b16332e2b73310d02e60db878e247619bc%22%3Bs%3A7%3A%22setTime%22%3Bi%3A1627886486%3B%7D; _TSKD=d5d7ee995c6ab3b7ec959da7abf906d4; BIQQ_TRACE_ID_COOKIE_NAME=a%3A1%3A%7Bs%3A11%3A%22BiqqTraceId%22%3Bs%3A32%3A%224410e2c8408562a1ddc419dc2ea9b569%22%3B%7D; __lt__cid=62334dd9-fe7a-46cb-a4b5-00e929b6a505; __lt__sid=00405372-593d0489; _gcl_au=1.1.1519616542.1627886492; _gid=GA1.2.1359109232.1627886492; _dc_gtm_UA-59214942-1=1; _gat_UA-2279884-63=1; __utma=248786310.1744952973.1627886492.1627886492.1627886492.1; __utmc=248786310; __utmz=248786310.1627886492.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _fbp=fb.1.1627886492317.1245845465; krt.vis=c6f6840e-de6d-487c-ae65-984ec169b5ef; FPID=FPID1.2.Foupz%2FfVCsYbiYk%2BWcgTBlxNnxvQTpkKuxZXefXiTp8%3D.1627886492; FPAU=1.1.1519616542.1627886492; __ulfpc=202108021441335187; krt.context=session%3Ab2ae8aaa-7239-4a92-b373-46fdf583a62a%3Bcontext_mode%3Aother; __pp_uid=zplUND2klgbZK6BujO59hoguDC09ZcDZ; _ts_yjad=1627886499944; _CBCA=a%3A1%3A%7Bs%3A3%3A%22rdt%22%3Bs%3A8%3A%2220210802%22%3B%7D; _td=8758287c-3217-4a20-9fe0-1b55bc9c0a2a; __utmb=248786310.2.10.1627886492; _ga=GA1.1.1744952973.1627886492; _ga_JL5LLXFB4P=GS1.1.1627886492.1.1.1627886517.0; stc114487=tsa:1627886492580.52314728.59060717.04476806531268385.:20210802071158|env:1%7C20210902064132%7C20210802071158%7C2%7C1039104:20220802064158|uid:1627886492579.1464788783.811739.114487.854537479.1:20220802064158|srchist:1039104%3A1%3A20210902064132:20220802064158'
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
            # 'Cookie': paramas['cookies'],
            'Host': 'p-bandai.jp',
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
            "paramas": paramas
        }

        if self.proxy:
            meta['proxy'] = f"http://{self.proxy['ip']}:{self.proxy['port']}"

        # return Request(url=url, callback=callback, headers=headers, meta=meta, dont_filter=True)
        return Request(url=url, callback=callback, headers=headers, meta=meta)

    def parse(self, response):
        paramas = response.meta['paramas']
        item = OutputItem()
        # # 商品名称
        goods_name = response.css('h1.productsname::text').extract_first()
        item["goods_name"] = goods_name or None
        item["goods_id"] = paramas["goods_id"]
        item["goods_url"] = response.url
        item["thedate"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        try:
            html_text = response.text
            goods_num_list = re.search('orderno_list = (.*?);', html_text, re.S).group(1)
            goods_no_dict = json.loads(goods_num_list)
            goods_no = goods_no_dict['0000000000']
            stock = re.search('.*?all_stock_out = (.*?);', html_text, re.S).group(1)
            order_maxnum = re.search('.*?ordermax_list = (.*?);', html_text, re.S).group(1)
            order_maxnum_dict = json.loads(order_maxnum)
            max_num = order_maxnum_dict[goods_no]
            if max_num == 0 and stock != "":
                item["goods_status"] = 0  # 无库存
            else:
                item["goods_status"] = 1  # 有库存
        except Exception as e:
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
