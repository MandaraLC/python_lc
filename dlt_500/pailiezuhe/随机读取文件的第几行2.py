#coding=utf-8
#! /usr/bin/python
import random
import linecache
def hello():
    count = len(open('alllist1-10/list1_20190415_2.txt','r').readlines())#获取行数
    hellonum=random.randrange(1,count, 1)#生成随机行数
    return linecache.getline('alllist1-10/list1_20190415_2.txt',hellonum)#随机读取某行
if __name__ == "__main__":
    with open('result.txt', 'a+') as f:
        for i in range(5):
            #print(hello())
            f.write(hello())
            #print(hello())

