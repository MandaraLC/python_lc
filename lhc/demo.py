import os

file = "./data/data.txt"
try:
    with open(file, 'r', encoding="utf-8-sig") as f:
        content = f.readlines()
except:
    with open(file, 'r') as f:
        content = f.readlines()

sum = 0 #总数
count = 0 #几次
te = 10
if content:
    for i in content:
        splitstr = i.split("各")
        splitstr1 = splitstr[1].split("计")

        print(splitstr[0]) #数据
        print(splitstr1)
        if splitstr[0].find(str(te)):
            count+=1

        sum+=int(splitstr1[1])

    print(f"总金额：{sum}\t次数：{count}")
else:
    print("没有数据")



