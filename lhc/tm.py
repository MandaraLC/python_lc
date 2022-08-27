file = "./data/data.txt"
try:
    with open(file, 'r', encoding="utf-8-sig") as f:
        content = f.readlines()
except:
    with open(file, 'r') as f:
        content = f.readlines()

sum = 0 #总金额
sumlist = [] #各单总金额列表
wincount = 0 #中奖单数
winsum = 0 #中奖金额
winlist = [] #中奖金额列表
tema = 10 #特码
if content:
    for i in content:
        print("数据：", i.strip())
        splitstr = i.strip().split("各")
        splitstr1 = splitstr[1].split("计")

        print("按各拆分：", splitstr) #数据
        print("按计拆分：", splitstr1)
        if splitstr[0].find(str(tema)) >= 0:
            wincount+=1
            winsum+= int(splitstr1[0])
            winlist.append(splitstr1[0])

        sum+= int(splitstr1[1])
        sumlist.append(splitstr1[1])
        print("=====================================================================================================")

    print(f"本期特码：{tema}")
    print("=================================")
    print(f"总单金额：共计{'+'.join(sumlist)}={sum}元")
    print("=================================")
    print(f"中特码{tema}的单数：共{wincount}单，共计：{'+'.join(winlist)}={winsum}元，共赔：{winsum} x 44={int(winsum)*44}元")
    print("=================================")
    print(f"返水共计：{sum}x0.10={sum*0.10}元")
    print("=================================")
    print(f"本期盈亏（总金额-中奖金额）：{sum}-{int(winsum)*44}={sum-(int(winsum)*44)}元")
else:
    print("没有数据")



