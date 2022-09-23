import os

#这是正确的
file = "./jiaoji/103/test1.txt"
try:
    with open(file, 'r', encoding="utf-8") as f:
        content = f.readlines()
except:
    with open(file, 'r') as f:
        content = f.readlines()

alldata = []
for i in content:
    slipt0 = i.strip().split(" ")
    slipt1 = slipt0[1].split(",")
    alldata.append(set(slipt1))

file0 = "./shaixuan/25shaixuan_data_103.txt"
try:
    with open(file0, 'r', encoding="utf-8") as f0:
        content0 = f0.readlines()
except:
    with open(file0, 'r') as f0:
        content0 = f0.readlines()

alldata0 = []
for a in content0:
    slipt2 = a.strip().split(" ")
    slipt3 = slipt2[1].split(",")
    alldata0.append(set(slipt3))

# print(alldata)
# print(alldata0)
# print(len(alldata))
# print(len(alldata0))
for b in alldata:
    for c in alldata0:

        jiaoji = b & c
        # if len(jiaoji) == 22:
        # print("list1：", b)
        # print("list2：", c)
        # print("交集：", jiaoji)
        print("长度：", len(jiaoji))
    print("=========================================")
#初始值
# data0 = alldata[0]
# data1 = alldata[1]
# data2 = (data0 & data1)
# print("列表1：", data0)
# print("列表2：", data1)
# print("两个列表交集：", data2, "长度：", len(data2))