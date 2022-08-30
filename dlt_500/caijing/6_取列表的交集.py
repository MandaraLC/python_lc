import os
#测试取多个列表的交集
# lst1 = [11, 22, 33]
# lst2 = [22, 33, 44]
# a = set(lst1)   # 转成元祖
# b = set(lst2)
# data = (a & b)  # 集合c和b中都包含了的元素
# print(data)

file = "./shaixuan/25shaixuan_data_100.txt"
with open(file, 'r') as f:
    content = f.readlines()

alldata = []
for i in content:
    slipt0 = i.strip().split(" ")
    slipt1 = slipt0[1].split(",")
    alldata.append(set(slipt1))

#将列表元素反转
# alldata.reverse()

filepath = "./jiaoji/100/30_jiaoji_data_100.txt"
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")

data = alldata[10]
for a in range(len(alldata)):
    if (a + 1) <= len(alldata) and len(data) > 0 and a >= 30:
    # if (a + 1) <= len(alldata) and len(data) > 0:
        print("列表1：", data)
        print("列表2：", alldata[a+1])
        # fileInput.write(f"列表1：{data}\n")
        # fileInput.write(f"列表2：{alldata[a + 1]}\n")
        data = (data & alldata[a+1])
        print("两个列表交集：", data)
        print("===========================")
        fileInput.write(f"两个列表交集：{data}\n")
        # fileInput.write("===========================\n")
