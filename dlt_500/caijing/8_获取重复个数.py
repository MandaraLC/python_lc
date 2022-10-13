#测试数据
# list0 = [11, 22, 33, 11, 45, 33, 35, 66]
# myset = set(list0)
# print(myset)
# datajson = {}
# for item in myset:
#     datajson[item] = list0.count(item)
# print(datajson)

file = "shaixuankill3/kill3_shaixuan_data_116.txt"
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

# 得到所有数据： ['08', '21', '31', '07', '03', '12', '15', '04', '07', '29', '13', '19', '23', '01', '21', '28', '10', '13', '25', '11', '18', '33', '01', '08', '16', '07', '18', '22', '02', '07', '19', '18', '21', '31', '05', '29', '31', '04', '08', '30', '06', '08', '13', '03', '07', '29', '02', '15', '29', '02', '14', '27', '17', '28', '29', '01', '09', '18', '03', '12', '16']
# 数据总个数： 61
# 排序后的数据 [('07', 5), ('29', 5), ('18', 4), ('08', 4), ('13', 3), ('21', 3), ('31', 3), ('02', 3), ('03', 3), ('01', 3), ('19', 2), ('16', 2), ('12', 2), ('15', 2), ('28', 2), ('04', 2), ('30', 1), ('27', 1), ('06', 1), ('33', 1), ('05', 1), ('23', 1), ('09', 1), ('17', 1), ('11', 1), ('25', 1), ('14', 1), ('10', 1), ('22', 1)]
