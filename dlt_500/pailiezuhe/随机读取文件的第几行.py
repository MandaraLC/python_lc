# encoding=utf-8
# 随机数，随机读取每一行的数据
import linecache
import random

#for i in range(1, 5):  # for循环几次
a = random.randrange(1, 18)  # 1-9中生成随机数
print(a)
# 从文件poem.txt中对读取第a行的数据
theline = linecache.getline(r'poem.txt', a)
print(theline)