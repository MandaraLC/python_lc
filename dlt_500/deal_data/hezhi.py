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
    filepath = "data/hezhi.txt"
    delfile(filepath)

    hezhi60to69 = 0
    hezhi70to79 = 0
    hezhi80to89 = 0
    hezhi90to99 = 0
    hezhi100to109 = 0
    hezhi110to119 = 0
    hezhi120to129 = 0
    hezhi130to139 = 0
    for data in content:
        slipt = data.strip().split(" ")
        sum = int(slipt[0])+int(slipt[1])+int(slipt[2])+int(slipt[3])+int(slipt[4])+int(slipt[5])
        if sum >=60 and sum <=69:
            hezhi60to69+=1
        if sum >=70 and sum <=79:
            hezhi70to79+=1
        if sum >=80 and sum <=89:
            hezhi80to89+=1
        if sum >=90 and sum <=99:
            hezhi90to99+=1
        if sum >=100 and sum <=109:
            hezhi100to109+=1
        if sum >=110 and sum <=119:
            hezhi110to119+=1
        if sum >=120 and sum <=129:
            hezhi120to129+=1
        if sum >=130 and sum <=139:
            hezhi130to139+=1
        writefile(sum, filepath)
    print('hezhi60to69：',hezhi60to69,
          '\thezhi70to79：',hezhi70to79,
          '\thezhi80to89：',hezhi80to89,
          '\thezhi90to99：',hezhi90to99,
          '\thezhi100to109：',hezhi100to109,
          '\thezhi110to119：', hezhi110to119,
          '\thezhi120to129：', hezhi120to129,
          '\thezhi130to139：', hezhi130to139
          )
    # hezhi60to69： 108 	hezhi70to79： 204 	hezhi80to89： 333 	hezhi90to99： 407
    # hezhi100to109： 437 	hezhi110to119： 358 	hezhi120to129： 241 	hezhi130to139： 128

else:
    print("没有数据！")