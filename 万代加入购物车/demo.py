import requests
#商品url
url = 'https://p-bandai.jp/item/item-1000180871/'
headers = {
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
rsp = requests.get(url=url, headers=headers)
print(rsp)
# 如果对方服务器给传送过来cookie信息，则可以通过反馈的cookie属性得到
# 返回一个cookiejar实例
cookiejar = rsp.cookies
# 可以讲cookiejar转换成字典
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookiedict)
exit()
headers = {
    "accept":"application/json, text/javascript, */*; q=0.01",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.9,ja;q=0.8",
    "content-type":"application/x-www-form-urlencoded",
    "origin":"https://p-bandai.jp",
    "referer":"https://p-bandai.jp/item/item-1000180871/",
    "sec-ch-ua-mobile":"?0",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
data = {
    "order":"2606408",
    "unit":"1",
    "model_no":"1000180871",
    "modelname":"METAL+BUILD+%E3%82%AC%E3%83%B3%E3%83%80%E3%83%A0%E3%83%87%E3%83%A5%E3%83%8A%E3%83%A1%E3%82%B9%EF%BC%86%E3%83%87%E3%83%B4%E3%82%A1%E3%82%A4%E3%82%BA%E3%83%87%E3%83%A5%E3%83%8A%E3%83%A1%E3%82%B9"
}
response = requests.post(
    url="https://p-bandai.jp/pb_cart_add.php",
    data=data,
    headers=headers,
    verify=False,
    timeout=5
)
print(response.text)