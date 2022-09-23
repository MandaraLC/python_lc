#测试数据
# list0 = [11, 22, 33, 11, 45, 33, 35, 66]
# myset = set(list0)
# print(myset)
# datajson = {}
# for item in myset:
#     datajson[item] = list0.count(item)
# print(datajson)

file = "shaixuankill3/kill3_shaixuan_data_110.txt"
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
#22110:09 13 15 18 20 28
#得到所有数据： ['05', '06', '28', '27', '31', '33', '33', '01', '21', '26', '05', '10', '20', '06', '20', '31', '08', '14', '31', '05', '21', '25', '14', '16', '27', '07', '25', '27', '21', '23', '26', '03', '20', '33', '02', '05', '25', '20', '28', '29', '04', '14', '33', '13', '22', '33', '01', '10', '16', '19', '26', '27', '08', '27', '33', '04', '13', '16', '03', '12', '32']
#数据总个数： 61
#排序后的数据 [('33', 6), ('27', 5), ('05', 4), ('20', 4), ('14', 3), ('25', 3), ('26', 3),
# ('31', 3), ('16', 3), ('21', 3), ('01', 2), ('13', 2), ('08', 2), ('28', 2), ('06', 2),
# ('03', 2), ('10', 2), ('04', 2), ('02', 1), ('29', 1), ('23', 1), ('32', 1), ('12', 1),
# ('22', 1), ('19', 1), ('07', 1)]

