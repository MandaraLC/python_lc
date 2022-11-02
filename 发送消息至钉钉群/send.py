from dingtalk import DingtalkMsgReport

at_who_mobiles = ['', '15112476096']  # 必须要加第一个 ''
at_content = '@'.join(at_who_mobiles)
content = '我是测试内容'
print(content+at_content)
exit()
# #马士基报错群
webhook = r'https://oapi.dingtalk.com/robot/send?access_token=48e527a6f883d558cd6a41e39589ddf6037f757c2032ffb8aa7ca0ded6fd3662'
secret = 'SEC45ac3158f2f0a6cc0f7e9c17b20edfa07a93c72a4bc5220fb698089fe341db6e'
report = DingtalkMsgReport(webhook=webhook, secret=secret)

name = '测试一下'
at_who_mobiles = ['', '15112476096']  # 必须要加第一个 ''
content = '我是测试内容'
at_content = '@'.join(at_who_mobiles)
report.chatbot_makedown(title='{platform} 消息通知'.format(platform=name), content=content+at_content, atMobiles=at_who_mobiles[1:])