from requests_html import HTMLSession
session = HTMLSession()

r = session.get('http://www.baidu.com')
r.html.render()  # 首次使用，自动下载chromium
print(r.text)