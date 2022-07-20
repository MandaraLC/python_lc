import os

# 写入文件
def writefile(msg, filepath):
    fileInput = open(filepath, "a")
    fileInput.write(''.join(msg) + '\n')

file = "../data/data_ssq.txt"
with open(file, 'r', encoding="utf-8-sig") as f:
    content = f.readlines()

if content:
    filepath = "data/weishu.txt"
    try:
        os.remove(filepath)
    except:
        pass
    
    len3 = 0
    len4 = 0
    len5 = 0
    len6 = 0
    for data in content:
        slipt = data.strip().split(" ")
        arr = []
        for i in slipt:
            if i[-1:] not in arr:
                arr.append(i[-1:])
        arr.sort()
        length = len(arr)
        if length == 3:
            len3+=1
        elif length == 4:
            len4 += 1
        elif length == 5:
            len5 += 1
        elif length == 6:
            len6 += 1
        writefile(' '.join(arr)+"="+str(length), filepath)
    print("3个尾数：", len3, "\t4个尾数：", len4, "\t5个尾数：", len5, "\t6个尾数：", len6)
    #3个尾数： 51 	4个尾数： 554 	5个尾数： 1200 	6个尾数： 552
else:
    print("没有数据！")