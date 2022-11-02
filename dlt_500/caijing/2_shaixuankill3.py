import os
file = "./yc/yc22122_数据2022-10-24.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = 'shaixuankill3/kill3_shaixuan_data_122.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    #if i.find("当前访问") >= 0 or i.find("===") >= 0
    # if (i.find("25码") >= 0 or i.find("20码") >= 0) or i.find("===") >= 0:
    if i.find("红球杀三码") >= 0:
        fileInput.write(f"{i.replace('：', ' ').strip()}\n")