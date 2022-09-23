import os

file = "./yc/yc22106_数据2022-09-13.txt"
with open(file, 'r') as f:
    content = f.readlines()

filepath = 'right_data/right_data_106.txt'
try:
    os.remove(filepath)
except:
    pass
fileInput = open(filepath, "a")

#17 20 22 23 24 31
for i in content:
    if i.find("===") >= 0 or (
            i.find("17") >= 0 and i.find("20") >= 0 and i.find("22") >= 0 and i.find("23") >= 0 and i.find(
            "24") >= 0 and i.find("31") >= 0):
        fileInput.write(f"{i.strip()}\n")
