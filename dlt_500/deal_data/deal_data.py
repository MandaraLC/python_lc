import os


# 写入文件
def writefile(msg, filepath):
    fileInput = open(filepath, "a")
    fileInput.write(str(msg) + '\n')

def delfile(filepath):
    # 文件存在则删除文件
    try:
        os.remove(filepath)
    except:
        pass

file = "../data/data_ssq.txt"
with open(file, 'r', encoding="utf-8-sig") as f:
    content = f.readlines()

if content:
    filepath = "./data/deal_data.txt"
    delfile(filepath)

    for data in content:
        slipt = data.strip().split(" ")
        #sum
        sum = int(slipt[0])+int(slipt[1])+int(slipt[2])+int(slipt[3])+int(slipt[4])+int(slipt[5])
        print("sum=", sum)
        #jiou
        ji = 0
        ou = 0
        #weishu
        weishu = []
        for i in slipt:
            if int(i) % 2 == 0:
                ou+=1
            else:
                ji+=1
            if i[-1:] not in weishu:
                weishu.append(i[-1:])
        weishu.sort()

        print("ji:ou=", ji, ":", ou)
        print('weishu=',weishu)
        print("=========================================")

else:
    print("没有数据！")