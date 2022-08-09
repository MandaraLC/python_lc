# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from crawl_haiwai_kc.spiders.bandai import BandaiSpider
from crawl_haiwai_kc.spiders.rakuten import RakutenSpider
from crawl_haiwai_kc.spiders.yahoo import YahooSpider
from crawl_haiwai_kc.spiders.yodobashi import YodobashiSpider
from crawl_haiwai_kc.tools import argsmodule
from scrapy.utils.project import get_project_settings
import os
from multiprocessing import Process


def main(class_name, mode, freq_min):
    process = CrawlerProcess(get_project_settings())
    process.crawl(class_name, mode=mode, freq_min=freq_min)
    process.start()    # the script will block here until all crawling jobs are finished


def get_args():
    # 获取命令行中的参数(账号, 密码, id)
    args_dict = {
        '-mode': {'help': 'mode', 'type': str, 'default': 'DEV'},
        '-freq_min': {'help': 'freq_min', 'type': int, 'default': 23},
    }
    args = argsmodule.get_args(args_dict)
    return args.mode, args.freq_min


# python ./crawl_haiwai_kc/run.py
if __name__ == '__main__':
    print('start')
    # 参数设置
    mode, freq_min = get_args()

    # name = [BandaiSpider, RakutenSpider, YahooSpider, YodobashiSpider]
    name = [BandaiSpider]

    for i in range(len(name)):
        p = Process(target=main, args=(name[i], mode, freq_min))
        p.start()
