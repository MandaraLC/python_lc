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


if "__main__" == __name__:

    # 测试
    # msg = 'test'
    # # report = MsgReport(msg=msg)
    # # report.classify_report()

    #马士基报错群
    webhook = r'https://oapi.dingtalk.com/robot/send?access_token=48e527a6f883d558cd6a41e39589ddf6037f757c2032ffb8aa7ca0ded6fd3662'
    secret = 'SEC45ac3158f2f0a6cc0f7e9c17b20edfa07a93c72a4bc5220fb698089fe341db6e'
    report = DingtalkMsgReport(webhook=webhook, secret=secret)

    # 名称id
    # print(report.chatbot_makedown(title='Test makedown',
    #                               content='### test121 \n 1\n @王俏敏Vivian(王俏敏Vivian)  2\n', atUserIds=['王俏敏Vivian(王俏敏Vivian)']))

    # print(report.chatbot_makedown(title='Test makedown',
    #                               content='### test121 \n 1\n @徐泽楷\n', atUserIds=['徐泽楷']))

    # # 电话id
    # print(report.chatbot_makedown(title='Test makedown',
    #                               content='### test121 \n 1\n 2\n @16620168836', atMobiles=['16620168836']))
    # for i in range(0, 30):
    #     print(report.chatbot_makedown(title='Test makedown',
    #                                   content='### 次数 \n id:{i} @16620168836 @18824161203'.format(i=i), atMobiles=['16620168836', '18824161203']))

    name = 'rakuma'
    at_who_mobiles = ['', '16620168836']  # 必须要加第一个 ''
    at_content = '@'.join(at_who_mobiles)
    items = [
        {
            'goods_id': 3,
            'goods_name': 'RIOBOT スーパーロボット大戦OG 変形合体 R-2パワード[千値練]《１０月予約》',
            'goods_status': '无货',
            'goods_url': 'https://item.rakuten.co.jp/amiami/figure-124233/',
            'thedate': '2021-04-28 11:39:07'
        },
        {
            'goods_id': 4,
            'goods_name': 'RIOBOT スーパーロボット》',
            'goods_status': '有货',
            'goods_url': 'https://item.rakuten.co.jp/amiami/figure-124233/',
            'thedate': '2021-04-28 11:39:07'
        }
    ]
    cache_message = ''
    for item in items:
        cachemessage = '- {goods_name}\n#### [状态:{state}]({url})\n###### 时间：{str_time}\n'.format(
            goods_name=item['goods_name'], state=item['goods_status'], str_time=item["thedate"], url=item['goods_url'])
        cache_message = cache_message + cachemessage

    at_who_mobiles = ['', '16620168836']
    at_content = '@'.join(at_who_mobiles)
    total_len = 2
    exchage_num = 1
    invalid_num = 0
    content = '### {platform}平台,总: ***{total}***, 变化: ***{exchange}***, 无效: ***{invalid}***\n{cachemessage}\n{at_content}'.format(total=total_len, exchange=exchage_num, invalid=invalid_num,
                                                                                                                                  platform=name, at_content=at_content, cachemessage=cache_message)

    print(report.chatbot_makedown(title='{platform}平台侦察'.format(
        platform=name), content=content, atMobiles=at_who_mobiles[1:]))
