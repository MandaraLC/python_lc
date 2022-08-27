import os
file = "./data/yc22099_数据2022-08-27.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './shaixuan/shaixuan_data_099.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    #if i.find("当前访问") >= 0 or i.find("===") >= 0
    if i.find("25码") >= 0 and i.find("当前访问") < 0:
        fileInput.write(f"{i.replace('：', ' ').strip()}\n")