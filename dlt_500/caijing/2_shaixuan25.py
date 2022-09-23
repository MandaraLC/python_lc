import os
file = "./yc/yc22110_数据2022-09-21.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = 'shaixuan25/25shaixuan_data_110.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    #if i.find("当前访问") >= 0 or i.find("===") >= 0
    # if (i.find("25码") >= 0 or i.find("20码") >= 0) or i.find("===") >= 0:
    if i.find("25码") >= 0:
        fileInput.write(f"{i.replace('：', ' ').strip()}\n")