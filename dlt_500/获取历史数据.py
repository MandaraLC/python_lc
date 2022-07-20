import requests
import re
def list_split(items, n):
    return [items[i:i+n] for i in range(0, len(items), n)]

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
# url = "https://datachart.500.com/dlt/history/history.shtml"
url = "https://datachart.500.com/dlt/history/newinc/history.php?start=20008&end=22037"
proxies = {
    'http':'115.28.220.135:9300'
}
respone = requests.get(url=url, headers=header, proxies=proxies)
respone_text = respone.text

#<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
#解决由于meta标签设置字体编码为gb2312，中文乱码的问题
respone_decode = respone_text.encode("latin1").decode("gbk")

#匹配tbody标签之间的数据
matchobj = re.findall('<tbody id="tdata">\n?\t?(.*)\n?\t?</tbody>', respone_decode)

#替换掉\t和\n
replace_str0 = matchobj[0].replace("\t","").replace("\n", "")

#替换掉注释(re.sub) 正则替换
replace_str1 = re.sub("<!--<td>\d+</td>-->","",replace_str0)

#匹配每个tr
matchobj1 = re.findall('<td class="cfont2">(\d+)</td>', replace_str1)

#将一个数组均匀切分成多个数组
list0 = list_split(matchobj1, 5)

#以w的方式打开文件，写入数据
fileInput = open("data.txt", "w")
for item in list0:
    fileInput.write(','.join(item)+"\n")









