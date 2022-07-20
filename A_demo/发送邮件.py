import smtplib  #加载smtplib模块
# from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def sendemail(subject="测试"):
    ret = True
    # try:
    my_sender = '1414801174@qq.com'  # 发送人
    my_user = 'liucheng@ingram-net.com'  # 接收人

    msg = MIMEMultipart()
    # msg = MIMEText("测试邮件", 'plain', 'utf-8')
    msg['From']=formataddr(["程序运行完成通知", my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["收件人", my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = subject #邮件的主题，也可以说是标题

    #发送附件
    att1 = MIMEApplication(open("./test.txt", 'rb').read())
    att1['Content-Type'] = 'application/octet-stream'
    #这里的filename可以任意写，写什么邮件就显示什么名字
    att1.add_header('Content-Disposition', 'attachment', filename="test.txt")
    msg.attach(att1)

    server = smtplib.SMTP("smtp.qq.com", 25)
    server.login(my_sender,"bmewmdzcrrbxjecc")    #发件人邮箱授权码 # 注意：这里不是密码，而应该填写授权码！！
    server.sendmail(my_sender,[my_user], msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()   #这句是关闭连接的意思
    # except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
    #     ret = False
    return ret

ret = sendemail()
if ret:
    print("发送成功！")
else:
    print("发送失败！")
