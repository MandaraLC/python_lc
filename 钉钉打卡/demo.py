import time
#获取当前时间
now = time.strftime("%H:%M:%S", time.localtime(time.time()))
print("当前时分秒：", now)

#下班时分秒
xbtime = '183000'
print(xbtime)

print(now < xbtime)