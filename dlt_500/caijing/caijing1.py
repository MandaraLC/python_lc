import time
import requests
import json
import os
from openpyxl import Workbook
from openpyxl import load_workbook
from lxml import etree

class Caijing:
    #初始化
    def __init__(self):
        ycqihao = self.getycqihao()
        self.replyfile = f'./yc/yc{ycqihao}_数据{time.strftime("%Y-%m-%d", time.localtime(time.time()))}.txt'
        try:
            os.remove(self.replyfile)
        except:
            pass

    def join_list(self, item):
        """处理列表到字符串"""
        return ",".join(item)

    #获取所预测的期号
    def getycqihao(self):
        header = {
            "Host": "datachart.500.com",
            "Content-Type": "text/html; charset=gb2312",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        # ssq
        url1 = 'https://datachart.500.com/ssq/history/history.shtml'

        respone1 = requests.get(url=url1, headers=header)
        html = etree.HTML(respone1.text)
        qihao = self.join_list(html.xpath("//input[@id='end']/@value"))
        return int(qihao)+1

    #获取每个预测种类的数据
    def getdatanums(self):
        get_data_api = 'https://www.cjcp.com.cn/index.php?m=Yuce&a=getdatanums'
        # zbname_arr = ['25hongdd']
        zbname_arr = ['hqshasanma']

        headers = {
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Host":"m.cjcp.com.cn",
            "Origin":"https://m.cjcp.com.cn",
            "Referer":"https://m.cjcp.com.cn/zhuanjia/ssq/",
            "sec-ch-ua-mobile":"?0",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
        }
        new_data = [] #生成的新数组

        for zb in zbname_arr:
            print('zbname：', zb)
            for page in range(10):
                post_data = {
                    "lotteryid": "1",
                    "childid": "4",
                    "zbname": zb,  # 20hongdd
                    #"names": "红球25码",
                    "sformf": "1",  # 1-免费 2-收费
                    "page": page+1  # 页数
                }

                respone_get_data = requests.post(url=get_data_api, data=post_data, headers=headers)
                jsons = json.loads(respone_get_data.text)
                print(f'第{page+1}页数据：', jsons)
                if jsons:
                    for data in jsons:
                        if data['aid'] is not None:
                            new_data_json = {
                                'userid':data['userid'],
                                'expertname':data['expertname'],
                                'aid':data['aid'],
                                'qs':data['qs'],
                                'lotteryid':data['lotteryid'],
                                'zhibiaoval':zb
                            }
                            new_data.append(new_data_json)
                            # fileInput = open(f"./data/{zb}.txt", "a")
                            # fileInput.write(str(new_data_json)+ "\n")
                    time.sleep(0.5)
                else:
                    break
            print("============================================")
        self.getdedaildata(new_data)

    #进入详情页获取数据
    def getdedaildata(self, new_data):
        print(f"共{len(new_data)}条数据，数据获取完成！以下是访问详情页面，并将数据写excel中...")
        dedail_page_header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "m.cjcp.com.cn",
            "Referer": "https://m.cjcp.com.cn",
            "sec-ch-ua-mobile": "?0",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
        }
        count = 1
        for data in new_data:
            detail_page_url = f"https://m.cjcp.com.cn/index.php?m=Recommend&a=wzListOne&type={data['expertname']}&zjid={data['aid']}&cb=0"
            print(f"当前访问第{count}条：", data['expertname'], detail_page_url)
            respone_detail_data = requests.get(url=detail_page_url, headers=dedail_page_header)
            html = etree.HTML(respone_detail_data.text)
            # print(respone_detail_data.text)
            # exit()
            items = html.xpath("//div[@class='yc_table']/table/tbody/tr")
            fileInput = open(self.replyfile, "a")
            # fileInput.write(f"{data['expertname']}\n")
            fileInput.write(f"=================={data['expertname']}=================\n")
            for item in items:
                zbname = item.xpath("./td[1]/text()")
                values = item.xpath("./td[2]/em/text()")
                if zbname:
                    if len(values) == 0:
                        values = item.xpath("./td[2]/span/text()")

                    fileInput.write(f"{self.join_list(zbname)} {self.join_list(values)}\n")

            count+=1
