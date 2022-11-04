import httpx
client = httpx.Client()

response = client.get(url="https://m.78500.cn/jiqiao/shuangseqiu/5487325.html",)

print(response.text)