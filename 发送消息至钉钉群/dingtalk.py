#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''

 修改
 * @version: 0.0.1
 * @Company:
 * @Author: stephen
 * @Last Modified by:   stephen
 * @Desc: 添加封装成类，根据返回的msg信息，自动化分类给响应的错误负责人
'''

import urllib
import requests

class DingtalkMsgReport(object):
    """
        钉钉群机器人
        参考文档：https://developers.dingtalk.com/document/app/custom-robot-access
    """

    def __init__(self, webhook=None, secret=None):
        params = dict(self._sign(secret))
        # 合并成webhookurl
        self.webhook = self._parse_webhook(webhook, params)

    def _parse_webhook(self, webhook, params):
        """
        @description  :
         合并webhookurl
        @param  :
          webhook: 正常url
          params： params 字典参数
        @Returns  :
            url
        """
        # print(params)
        return self.__add_url_params(url=webhook, params=params)

    def __add_url_params(self, url, params):
        """ Add GET params to provided URL being aware of existing.

        :param url: string of target URL
        :param params: dict containing requested params to be added
        :return: string with updated URL

        >> url = 'http://stackoverflow.com/test?answers=true'
        >> new_params = {'answers': False, 'data': ['some','values']}
        >> add_url_params(url, new_params)
        'http://stackoverflow.com/test?data=some&data=values&answers=false'
        """
        # Unquoting URL first so we don't loose existing args
        url = urllib.parse.unquote(url)
        # Extracting url info
        parsed_url = urllib.parse.urlparse(url)
        # Extracting URL arguments from parsed URL
        get_args = parsed_url.query
        # Converting URL arguments to dict
        parsed_get_args = dict(urllib.parse.parse_qsl(get_args))
        # Merging URL arguments dict with new params
        parsed_get_args.update(params)

        # Bool and Dict values should be converted to json-friendly values
        # you may throw this part away if you don't like it :)
        parsed_get_args.update(
            {k: dumps(v) for k, v in parsed_get_args.items()
             if isinstance(v, (bool, dict))}
        )

        # Converting URL argument to proper query string
        encoded_get_args = urllib.parse.urlencode(parsed_get_args, doseq=True)
        # Creating new parsed result object based on provided with new
        # URL arguments. Same thing happens inside of urlparse.
        new_url = urllib.parse.ParseResult(
            parsed_url.scheme, parsed_url.netloc, parsed_url.path,
            parsed_url.params, encoded_get_args, parsed_url.fragment
        ).geturl()

        return new_url

    def _sign(self, secret=None):
        """
        @description  :
            计算签名
        @param  :
            secret : 加签
        @Returns  :
            字典：参数
            sign：签名
            timestamp :时间戳
        """
        import time
        import hmac
        import hashlib
        import base64
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                             digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return {'sign': sign, 'timestamp': timestamp}

    def chatbot_text(self, touser=[], content=None):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "msgtype": "text",
            "text": {
                "content": content,
            }
        }
        result = requests.post(self.webhook, json=data, headers=headers)
        return result

    def chatbot_makedown(self, title=None, content=None, atMobiles=[], atUserIds=[], isAtAll=False):
        """
        @description  :
            makedown 类型文本发送
        @param  :
            {
                "msgtype": "markdown",
                "markdown": {
                    "title":"杭州天气",
                    "text": "#### 杭州天气 @150XXXXXXXX \n> 9度，西北风1级，空气良89，相对温度73%\n> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n> ###### 10点20分发布 [天气](https://www.dingtalk.com) \n"
                },
                "at": {
                    "atMobiles": [
                        "150XXXXXXXX"
                    ],
                    "atUserIds ": [
                        "user123"
                    ],
                    "isAtAll": false
                }
            }
        @Returns  :
            Response 结果
        """

        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": content,
            },
            "at": {
                "atMobiles": atMobiles,
                "atUserIds ": atUserIds,
                "isAtAll": isAtAll
            }
        }
        result = requests.post(self.webhook, json=data, headers=headers)
        return result