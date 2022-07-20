import requests
from lxml import etree
#处理https警告
requests.packages.urllib3.disable_warnings()

# 获取文本: //标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../text()
# 获取属性: //标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../@属性

def join_list(item):
    return "".join(item)

header = {
    "Host":"datachart.500.com",
    "Content-Type":"text/html; charset=gb2312",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9"
}
#dlt
url1 = "https://datachart.500.com/dlt/history/history.shtml"
respone1 = requests.get(url=url1, headers=header, verify=False)
html = etree.HTML(respone1.text)
qihao = join_list(html.xpath("//input[@id='end']/@value"))
print(qihao)

url = f"https://datachart.500.com/dlt/history/newinc/history.php?start=07001&end={qihao}"
respone = requests.get(url=url, headers=header, verify=False)
respone_decode = respone.text

#<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
#解决由于meta标签设置字体编码为gb2312，中文乱码的问题
# respone_decode = respone_decode.encode("latin1").decode("gbk")
# print(respone_decode)

html = etree.HTML(respone_decode)
trlist = html.xpath("//tbody[@id='tdata']/tr")

result_list = []
for item in trlist:
    result_list.append(
        {
            "qihao": join_list(item.xpath("./td[1]/text()")),
            "number":join_list(item.xpath("./td[2]/text()"))
                     +" "+join_list(item.xpath("./td[3]/text()"))
                     + " " + join_list(item.xpath("./td[4]/text()"))
                     + " " + join_list(item.xpath("./td[5]/text()"))
                     + " " + join_list(item.xpath("./td[6]/text()"))
                     + "    " + join_list(item.xpath("./td[7]/text()"))
                     + " " + join_list(item.xpath("./td[8]/text()"))
        }
    )
#以w的方式打开文件，写入数据
fileInput = open("data_dlt.txt", "w")
for item in result_list:
    fileInput.write(''.join(item['qihao']+":"+item['number'])+"\n")
