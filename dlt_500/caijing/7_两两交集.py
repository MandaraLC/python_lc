import os

file = "./jiaoji/103/test.txt"
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
    # alldata.append(slipt1)

filepath = "./jiaoji/103/jiaoji_data_103.txt"
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")

#初始值
data0 = alldata[0]
data1 = alldata[1]
data2 = (data0 & data1)
print("列表1：", data0)
print("列表2：", data1)
print("两个列表交集：", data2, "长度：", len(data2))
#21 18 21 20 21 18
#20 21 21 19 20
#19 20 19 21
#21 18 20
#17 22
#18
#===============================
#19 19
exit()
for a in range(len(alldata)):
    # if (a + 1) <= len(alldata) and len(data) > 0 and a >= 30:
    if (a + 1) <= len(alldata) and len(data) > 0:
        print(a+1)
        print("列表1：", data)
        print("列表2：", alldata[a+1])
        # fileInput.write(f"列表1：{data}\n")
        # fileInput.write(f"列表2：{alldata[a + 1]}\n")
        data = (data & alldata[a+1])
        print("两个列表交集：", data)
        print("===========================")
        fileInput.write(f"{data}\n")
        # fileInput.write("===========================\n")