import os

file = "./data/yc22092_数据2022-08-11.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './right_data_092.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    if i.find("当前访问") >= 0 or i.find("===") >= 0 or (
            i.find("07") >= 0 and i.find("10") >= 0 and i.find("16") >= 0 and i.find("20") >= 0 and i.find(
            "21") >= 0 and i.find("27") >= 0):
        fileInput.write(f"{i.strip()}\n")
