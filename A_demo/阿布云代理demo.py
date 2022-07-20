import httpx

def main():
    headers = {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30'}

    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"
    proxyUser = "HWV7KTNCWFD6UC8D"
    proxyPass = "87BC592154427AD7"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxies = {
        "http://"  : proxyMeta,
        "https://" : proxyMeta,
    }

    with httpx.Client(headers=headers, timeout=30, proxies=proxies) as client:
        resp = client.get('https://httpbin.org/ip')
        print(resp.json())

        # resp = client.get("https://test.abuyun.com/")
        # print(resp.text)
if __name__ == '__main__':
    main()