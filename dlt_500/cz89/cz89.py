import time
import requests
import json
import os
from openpyxl import Workbook
from openpyxl import load_workbook
from lxml import etree

class Cz89:
    #初始化
    def __init__(self):
        self.sheetnames = ['红球独胆', '红球双胆', '红球三胆', '红球12码', '红球20码', '红球25码', '红球杀三码', '红球杀六码',
                           '红球龙头两码', '红球凤尾两码', '蓝球定三码','蓝球定五码', '蓝球杀五码']
        ycqihao = self.getycqihao()
        filename = f'yc{ycqihao}_数据{time.strftime("%Y-%m-%d", time.localtime(time.time()))}.xlsx'
        self.filepath = f'./excel/{filename}'

        self.replyfile = f'./data/yc{ycqihao}_重复个数{time.strftime("%Y-%m-%d", time.localtime(time.time()))}.txt'
        try:
            os.remove(self.filepath)
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
        get_data_api = 'https://m.cjcp.com.cn/index.php?m=Yuce&a=getdatanums'
        # 25-25hongdd 20-20hongdd 12-hqshierma 1-hongqdudan 2-hqshuangdan 3-hqsandan k3-hqshasanma k6-shalh longtou2-hqltliangma
        #fengwei2-hqfwliangma lan3-smdl lan5-lqdingwuma lankill5-shawl
        # zbname_arr = ['25hongdd', '20hongdd', 'hqshierma', 'hongqdudan', 'hqshuangdan', 'hqsandan', 'hqshasanma',
        #               'shalh', 'hqltliangma', 'hqfwliangma', 'smdl', 'lqdingwuma', 'shawl']
        zbname_arr = ['25hongdd']

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
        for data in new_data:
            detail_page_url = f"https://m.cjcp.com.cn/index.php?m=Recommend&a=wzListOne&type={data['expertname']}&zjid={data['aid']}&cb=0"
            print("当前访问：", data['expertname'], detail_page_url)
            respone_detail_data = requests.get(url=detail_page_url, headers=dedail_page_header)
            html = etree.HTML(respone_detail_data.text)
            items = html.xpath("//div[@class='yc_table']/table/tbody/tr")
            for item in items:
                zbname = item.xpath("./td[1]/text()")
                values = item.xpath("./td[2]/em/text()")
                if zbname:
                    if len(values) == 0:
                        values = item.xpath("./td[2]/span/text()")

                    self.excel(self.join_list(zbname), data['expertname'], self.join_list(values))
        #获取各个元素的重复个数
        print("===========================================")
        self.getrepeatdata_count()

    #获取数据的重复个数
    def getrepeatdata_count(self):
        print("以下是获取各个sheet中的重复数据的个数...")
        excel = load_workbook(self.filepath)
        all_sheet = excel.sheetnames
        for i in all_sheet:
            old_order = []
            for column in excel[i].iter_cols():
                for cell2 in column:

                    if cell2.value is not None and cell2.row > 1 and cell2.column == 2:
                        # print(cell2.row, cell2.column, cell2.value)
                        if cell2.value.find(",") >= 0:
                            split0 = cell2.value.split(",")
                            for a in split0:
                                old_order.append(a)
                        else:
                            old_order.append(cell2.value)

            myset = set(old_order)
            datajson = {}
            for item in myset:
                datajson[item] = old_order.count(item)
            # 降序排序
            desc_data = sorted(datajson.items(), key=lambda x: x[1], reverse=True)
            if desc_data:
                print(i, "：", desc_data)
                fileInput = open(self.replyfile, "a")
                fileInput.write(f"{i}：{str(desc_data)}\n")

    #写入文件
    def excel(self, name, expertname, value):
        # 写入excel文件
        infolist = []
        infolist.append(expertname)
        infolist.append(value)
        if os.path.exists(self.filepath):
            workbook = load_workbook(filename=self.filepath)
        else:
            workbook = Workbook()
        workbook[name].append(infolist)
        workbook.save(filename=self.filepath)

    # 初始化excel
    def initexcel(self):
        # 表头
        tatal = ['昵称', '数据']
        if os.path.exists(self.filepath):
            workbook = load_workbook(filename=self.filepath)
        else:
            workbook = Workbook()

        for key, value in enumerate(self.sheetnames):
            # 创建sheet
            workbook.create_sheet(value, key)
            workbook[self.sheetnames[key]].append(tatal)
            workbook.save(filename=self.filepath)