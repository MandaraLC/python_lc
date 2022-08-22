import os

file = "./data/yc22096_数据2022-08-19.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './right_data_096.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    if i.find("当前访问") >= 0 or i.find("===") >= 0 or (
            i.find("03") >= 0 and i.find("16") >= 0 and i.find("17") >= 0 and i.find("19") >= 0 and i.find(
            "25") >= 0 and i.find("33") >= 0):
        fileInput.write(f"{i.strip()}\n")
