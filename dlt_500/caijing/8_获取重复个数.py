#测试数据
# list0 = [11, 22, 33, 11, 45, 33, 35, 66]
# myset = set(list0)
# print(myset)
# datajson = {}
# for item in myset:
#     datajson[item] = list0.count(item)
# print(datajson)

file = "shaixuankill3/kill3_shaixuan_data_117.txt"
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
# 得到所有数据： ['02', '04', '23', '18', '21', '29', '01', '04', '18', '15', '24', '31', '06', '09', '26', '06', '26', '31', '01', '26', '31', '01', '16', '17', '03', '23', '24', '15', '24', '32', '07', '18', '32', '14', '24', '29', '07', '27', '29', '07', '12', '31', '12', '20', '23', '05', '21', '33', '03', '19', '22', '13', '18', '27', '15', '20', '30', '11', '12', '23', '03', '05', '24']
# 数据总个数： 63
# 排序后的数据 [('24', 5), ('31', 4), ('18', 4), ('23', 4), ('01', 3), ('15', 3), ('29', 3), ('26', 3), ('07', 3), ('12', 3), ('03', 3), ('20', 2), ('05', 2), ('32', 2), ('04', 2), ('27', 2), ('21', 2), ('06', 2), ('11', 1), ('22', 1), ('19', 1), ('17', 1), ('30', 1), ('16', 1), ('02', 1), ('33', 1), ('13', 1), ('09', 1), ('14', 1)]
