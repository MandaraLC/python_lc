import os

file = "./data/yc22099_数据2022-08-27.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './right_data/right_data_099.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    if i.find("当前访问") >= 0 or i.find("===") >= 0 or (
            i.find("01") >= 0 and i.find("11") >= 0 and i.find("23") >= 0 and i.find("24") >= 0 and i.find(
        "26") >= 0 and i.find("32") >= 0):
        fileInput.write(f"{i.strip()}\n")
