import os

file = "./yc/yc22100_数据2022-08-30.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = 'right_data/right_data_100.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")
for i in content:
    if i.find("===") >= 0 or (
            i.find("02") >= 0 and i.find("06") >= 0 and i.find("07") >= 0 and i.find("15") >= 0 and i.find(
            "20") >= 0 and i.find("21") >= 0):
        fileInput.write(f"{i.strip()}\n")
