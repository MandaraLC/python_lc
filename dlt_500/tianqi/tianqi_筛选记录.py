import os

file = "./data/yc22098_数据2022-08-25.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = './right_data/right_data_098.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")

for i in content:
    if i.find("当前访问") >= 0 or i.find("===") >= 0 or (
            i.find("02") >= 0 and i.find("03") >= 0 and i.find("04") >= 0 and i.find("06") >= 0 and i.find(
        "21") >= 0 and i.find("33") >= 0):
        fileInput.write(f"{i.strip()}\n")
