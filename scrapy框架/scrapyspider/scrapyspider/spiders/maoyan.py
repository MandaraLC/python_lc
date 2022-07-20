import scrapy
from lxml import etree

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['www.maoyan.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        html = etree.HTML(response.text)
        print("".join(html.xpath("//input[@class='bg s_btn']/@value")))
