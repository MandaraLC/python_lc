#测试数据
# list0 = [11, 22, 33, 11, 45, 33, 35, 66]
# myset = set(list0)
# print(myset)
# datajson = {}
# for item in myset:
#     datajson[item] = list0.count(item)
# print(datajson)

file = "shaixuankill3/kill3_shaixuan_data_122.txt"
with open(file, 'r') as f:
    content = f.readlines()

newlist = []
count = 0
for i in content:
    if count <= 20:
    # if count <= 10:
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

# 得到所有数据： ['04', '07', '19', '02', '04', '17', '22', '26', '30', '14', '26', '27', '08', '20', '23', '17', '19', '28', '10', '12', '21', '09', '18', '20', '06', '07', '22', '10', '22', '29', '22', '26', '32', '03', '08', '21', '03', '28', '33', '06', '22', '31', '02', '04', '17', '18', '19', '21', '05', '24', '31', '05', '06', '27', '03', '04', '31', '01', '05', '08', '09', '13', '20']
# 数据总个数： 63
# 排序后的数据 [('22', 5), ('04', 4), ('31', 3), ('17', 3), ('08', 3), ('26', 3), ('03', 3), ('05', 3), ('06', 3), ('19', 3), ('20', 3), ('21', 3), ('07', 2), ('10', 2), ('28', 2), ('27', 2), ('18', 2), ('09', 2), ('02', 2), ('12', 1), ('29', 1), ('14', 1), ('23', 1), ('01', 1), ('24', 1), ('33', 1), ('32', 1), ('30', 1), ('13', 1)]
