from caijing import Caijing
import time
import os

filename = f'数据{time.strftime("%Y-%m-%d", time.localtime(time.time()))}.xlsx'
filepath = f'./excel/{filename}'
try:
    os.remove(filepath)
    os.remove(f'./data/重复个数{time.strftime("%Y-%m-%d", time.localtime(time.time()))}.txt')
except:
    pass
caijingobj = Caijing(filepath=filepath)
#初始化
caijingobj.initexcel()
#执行程序
caijingobj.getdatanums()