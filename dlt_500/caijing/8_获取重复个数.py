#测试数据
# list0 = [11, 22, 33, 11, 45, 33, 35, 66]
# myset = set(list0)
# print(myset)
# datajson = {}
# for item in myset:
#     datajson[item] = list0.count(item)
# print(datajson)

file = "shaixuankill3/kill3_shaixuan_data_113.txt"
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

# 得到所有数据： ['17', '13', '24', '31', '02', '14', '16', '21', '22', '28', '30', '32', '33', '25', '29', '32', '14', '28', '33', '12', '18', '31', '03', '18', '23', '02', '21', '30', '14', '22', '32', '07', '15', '17', '19', '26', '33', '03', '13', '24', '15', '30', '32', '04', '10', '33', '04', '18', '28', '03', '09', '28', '04', '07', '12', '03', '08', '21', '10', '11', '17']
# 数据总个数： 61
# 排序后的数据 [('03', 4), ('32', 4), ('28', 4), ('33', 4), ('18', 3), ('04', 3), ('30', 3), ('21', 3), ('14', 3), ('17', 3), ('12', 2), ('13', 2), ('02', 2), ('15', 2), ('07', 2), ('22', 2), ('24', 2), ('31', 2), ('10', 2), ('26', 1), ('08', 1), ('19', 1), ('11', 1), ('29', 1), ('16', 1), ('23', 1), ('25', 1), ('09', 1)]
