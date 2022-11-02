import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.application import MIMEApplication
import config

# 发送邮件
def sendemail(subject, filepath, filename, reciver):
    msg = MIMEMultipart()
    msg['From'] = formataddr(["chengxuyunxing", config.SENDER])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["shoujianren", reciver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = subject+str(time.time())  # 邮件的主题，也可以说是标题
    # 发送附件
    att1 = MIMEApplication(open(filepath, 'rb').read())
    att1['Content-Type'] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么邮件就显示什么名字
    att1.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(att1)

    smtpObj = smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT)
    smtpObj.connect(config.SMTP_HOST)
    smtpObj.login(config.SENDER, config.EMAIL_CODE)
    smtpObj.sendmail(config.SENDER, [reciver], msg.as_string())
    smtpObj.close()

filename = 'test1.txt'
filepath = f'./{filename}'
for i in config.RECIVER:
    result = sendemail("modifypwd", filepath, filename, i)
    print(result)
    time.sleep(1)