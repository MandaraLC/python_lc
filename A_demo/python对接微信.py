#安装相关库
# pip install itchat
# pip install echarts-python
import itchat
import re
import time

#实现登陆状态保存
itchat.auto_login(hotReload=True)
itchat.dump_login_status()

"""
# 发送消息，filehelper是微信上的文件传输助手。
itchat.send(u'你好呀43436', 'filehelper')
"""

"""
# 调用微信接口发送消息
userinfo = itchat.search_friends("绿叶一片")
userid = userinfo[0]["UserName"]   # 获取用户id
itchat.send("hello dear", userid)  # 通过用户id发送信息
# 或
itchat.send_msg(msg='hello dear', toUserName=userid)  # 发送纯文本信息
"""

"""
# 男女所占比例
friends = itchat.get_friends(update=True)[:]
print(friends[0])

total = len(friends) - 1
male = female = other = 0
for friend in friends[1:]:
    sex = friend["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
print("男性好友：%.2f%%" % (float(male) / total * 100))
print("女性好友：%.2f%%" % (float(female) / total * 100))
print("其他：%.2f%%" % (float(other) / total * 100))
"""


#个性签名
friends = itchat.get_friends(update=True)[:]
signature_list = []
for friend in friends:
    sex = friend["Sex"]
    sexname = ''
    if sex == 1:
        sexname = "男"
    elif sex == 2:
        sexname = "女"
    else:
        sexname = "保密"
    signature = friend["Signature"].strip()
    signature = re.sub("<span.*>", "", signature)
    jsondata = "昵称："+friend['NickName']+"\t性别："+sexname+"\t位置："+friend['Province']+"-"+friend['City']+"\t签名："+signature
    signature_list.append(jsondata)
    raw_signature_string = '\n'.join(signature_list)

print(raw_signature_string)


"""
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])), msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        # 回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])

if __name__ == '__main__':
    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()
"""


"""
{'MemberList': <ContactList: []>, 
'UserName': '@2fdc434d02eaa256878ba0c27e9b6ee7fc4f6c2ec8e3cbfdebc8624807e86e83', 
'City': '广州',
'DisplayName': '', 
'PYQuanPin': 'spanclassemojiemoji1f340span', 
'RemarkPYInitial': '', 'Province': '广东', 
'KeyWord': '', 
'RemarkName': '',
'PYInitial': 'SPANCLASSEMOJIEMOJI1F340SPAN',
'EncryChatRoomId': '',
'Alias': '', 
'Signature':
'愿我们一切都安好<span class="emoji emoji1f47b"></span>',
'NickName': '🍀',
'RemarkPYQuanPin': '',
'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=756272222&username=@2fdc434d02eaa256878ba0c27e9b6ee7fc4f6c2ec8e3cbfdebc8624807e86e83&skey=@crypt_3616f260_d68f1b30e96c504ec11c6d00cd8bef8e',
'UniFriend': 0,
'Sex': 1,
'AppAccountFlag': 0,
'VerifyFlag': 0, 
'ChatRoomId': 0,
'HideInputBarFlag': 0, 'AttrStatus': 105341,
'SnsFlag': 1, 'MemberCount': 0, 'OwnerUin': 0, 'ContactFlag': 2051,
'Uin': 649535414, 'StarFriend': 0, 'Statues': 0, 
'WebWxPluginSwitch': 0, 'HeadImgFlag': 1,
'IsOwner': 0
}
"""