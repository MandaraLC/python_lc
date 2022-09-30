#测试数据
# list0 = [11, 22, 33, 11, 45, 33, 35, 66]
# myset = set(list0)
# print(myset)
# datajson = {}
# for item in myset:
#     datajson[item] = list0.count(item)
# print(datajson)

file = "shaixuankill3/kill3_shaixuan_data_114.txt"
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

# 得到所有数据： ['15', '18', '30', '11', '12', '14', '06', '11', '33', '10', '15', '32', '07', '19', '28', '01', '19', '24', '02', '25', '32', '07', '09', '14', '12', '20', '21', '11', '16', '31', '06', '11', '29', '12', '21', '29', '01', '30', '31', '19', '25', '28', '05', '11', '16', '01', '02', '28', '04', '05', '17', '01', '03', '33', '09', '15', '28', '06', '25', '31', '03', '29', '31']
# 数据总个数： 63
# 排序后的数据 [('11', 5), ('31', 4), ('01', 4), ('28', 4), ('15', 3), ('25', 3), ('06', 3), ('12', 3), ('19', 3), ('29', 3), ('05', 2), ('07', 2), ('02', 2), ('21', 2), ('16', 2), ('30', 2), ('33', 2), ('32', 2), ('03', 2), ('09', 2), ('14', 2), ('18', 1), ('10', 1), ('17', 1), ('20', 1), ('24', 1), ('04', 1)]
