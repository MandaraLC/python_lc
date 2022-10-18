#测试数据
# list0 = [11, 22, 33, 11, 45, 33, 35, 66]
# myset = set(list0)
# print(myset)
# datajson = {}
# for item in myset:
#     datajson[item] = list0.count(item)
# print(datajson)

file = "shaixuankill3/kill3_shaixuan_data_119.txt"
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
# 得到所有数据： ['13', '27', '28', '20', '26', '27', '01', '10', '26', '16', '28', '31', '19', '26', '27', '01', '27', '33', '04', '11', '28', '14', '23', '32', '02', '04', '17', '16', '18', '22', '02', '20', '30', '02', '10', '26', '03', '18', '32', '24', '26', '27', '10', '18', '33', '01', '04', '06', '01', '17', '24', '07', '09', '30', '14', '20', '23', '06', '22', '30', '01', '06', '33']
# 数据总个数： 63
# 排序后的数据 [('27', 5), ('26', 5), ('01', 5), ('30', 3), ('33', 3), ('04', 3), ('10', 3), ('06', 3), ('28', 3), ('02', 3), ('20', 3), ('18', 3), ('23', 2), ('32', 2), ('24', 2), ('22', 2), ('17', 2), ('14', 2), ('16', 2), ('31', 1), ('13', 1), ('03', 1), ('11', 1), ('09', 1), ('07', 1), ('19', 1)]
