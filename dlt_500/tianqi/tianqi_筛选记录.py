import os

file = "./data/yc22091_数据2022-08-11.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './right_data_092.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")

for i in content:
    if i.find("当前访问") >= 0 or i.find("===") >= 0 or (i.find("08") >= 0 and i.find("18") >= 0 and i.find("20") >= 0 and i.find("22") >= 0 and i.find("24") >= 0 and i.find("28") >= 0):
        fileInput.write(f"{i.strip()}\n")
