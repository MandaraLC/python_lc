#测试数据
# list0 = [11, 22, 33, 11, 45, 33, 35, 66]
# myset = set(list0)
# print(myset)
# datajson = {}
# for item in myset:
#     datajson[item] = list0.count(item)
# print(datajson)

file = "shaixuankill3/kill3_shaixuan_data_112.txt"
with open(file, 'r') as f:
    content = f.readlines()

newlist = []
count = 0
for i in content:
    if count <= 20:
        slipt0 = i.strip().split(" ")
        slipt1 = slipt0[1].split(",")
        for i in slipt1:
            newlist.append(i)
        count+=1
    else:
        break

print("得到所有数据：", newlist)
print("数据总个数：", len(newlist))

datajson = {}
for item in set(newlist):
    datajson[item] = newlist.count(item)

# 降序排序
desc_data = sorted(datajson.items(), key=lambda x: x[1], reverse=True)
print("排序后的数据", desc_data)

# 得到所有数据： ['01', '23', '24', '04', '16', '29', '01', '07', '26', '13', '20', '27', '24', '26', '30', '11', '12', '30', '16', '19', '22', '02', '07', '18', '15', '20', '29', '16', '20', '27', '04', '05', '24', '05', '14', '22', '07', '25', '32', '05', '12', '33', '01', '13', '30', '09', '17', '27', '02', '22', '23', '05', '07', '19', '04', '07', '20', '09', '15', '23', '06', '11', '13']
# 数据总个数： 63
# 排序后的数据 [('07', 5), ('20', 4), ('05', 4), ('22', 3), ('27', 3), ('23', 3), ('16', 3), ('04', 3), ('30', 3), ('13', 3), ('01', 3), ('24', 3), ('02', 2), ('09', 2), ('19', 2), ('11', 2), ('15', 2), ('26', 2), ('29', 2), ('12', 2), ('25', 1), ('33', 1), ('14', 1), ('18', 1), ('17', 1), ('32', 1), ('06', 1)]

