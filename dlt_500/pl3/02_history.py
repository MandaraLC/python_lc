from lxml import etree
import httpx

# 获取文本: //标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../text()
# 获取属性: //标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../@属性
def join_list(item):
    return "".join(item)

header = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.9,ja;q=0.8",
    "cache-control":"max-age=0",
    "sec-ch-ua-mobile":"?0",
    "sec-fetch-dest":"document",
    "sec-fetch-mode":"navigate",
    "sec-fetch-site":"none",
    "sec-fetch-user":"?1",
    "upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
}
#ssq
url1 = 'https://datachart.500.com/pls/history/inc/history.php'

client = httpx.Client()
respone1 = client.get(url=url1, headers=header)
html = etree.HTML(respone1.text)
qihao = join_list(html.xpath("//input[@id='end']/@value"))
print("pl3最新：", qihao)

url = f'https://datachart.500.com/pls/history/inc/history.php?limit=6000&end={qihao}'
print(url)
respone = client.get(url=url, headers=header)
respone_decode = respone.text
# print(respone_decode)
html = etree.HTML(respone_decode)
trlist = html.xpath("//div[@class='chart']/table/tr")

result_list = []
for key,item in enumerate(trlist):
    if key > 1:
        result_list.append(
            {
                "qihao": join_list(item.xpath("./td[1]/text()")),
                "number":join_list(item.xpath("./td[2]/text()"))
            }
        )
#以w的方式打开文件，写入数据
fileInput = open("./data/data_pl3.txt", "w")
for item in result_list:
    # fileInput.write(''.join(item['qihao']+":"+item['number'])+"\n")
    fileInput.write(''.join(item['number']) + "\n")
