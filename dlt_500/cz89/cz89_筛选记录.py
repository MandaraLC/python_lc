import os

file = "./data/yc22100_数据2022-08-30.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './right_data/right_data_100.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    if i.find("当前访问") >= 0 or i.find("===") >= 0 or (
            i.find("04") >= 0 and i.find("16") >= 0 and i.find("18") >= 0 and i.find("19") >= 0 and i.find(
        "27") >= 0 and i.find("27") >= 0):
        fileInput.write(f"{i.strip()}\n")
