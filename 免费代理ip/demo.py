import requests
proxies = {"http": "http://124.156.141.229:15118", "https": "http://124.156.141.229:15118"}
response = requests.get("http://example.org", proxies=proxies)
print(response.text)