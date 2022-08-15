import os

file = "./data/yc22093_数据2022-08-12.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './right_data_093.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    if i.find("当前访问") >= 0 or i.find("===") >= 0 or (
            i.find("21") >= 0 and i.find("22") >= 0 and i.find("24") >= 0 and i.find("28") >= 0 and i.find(
            "29") >= 0 and i.find("32") >= 0):
        fileInput.write(f"{i.strip()}\n")
