#1.先筛选出25码，再去掉包含kill3的数据，最后取交集
import os
file = "./shaixuan25/25shaixuan_data_110.txt"
with open(file, 'r') as f:
    content = f.readlines()
print(f"共{len(content)}条数据")
kill3list = []
kill3set = [('03', 4), ('32', 4), ('28', 4), ('33', 4), ('18', 3), ('04', 3), ('30', 3), ('21', 3), ('14', 3), ('17', 3), ('12', 2), ('13', 2), ('02', 2), ('15', 2), ('07', 2), ('22', 2), ('24', 2), ('31', 2), ('10', 2), ('26', 1), ('08', 1), ('19', 1), ('11', 1), ('29', 1), ('16', 1), ('23', 1), ('25', 1), ('09', 1)]
for i in kill3set:
    kill3list.append(i[0])

print(kill3list)
print(len(kill3list))
lists = []
for a in content:
    status = 0
    for b in kill3list:
        #是否在这个列表中
        if a.find(str(b)) >= 0:
            status = 1
            break
    if status == 0:
        lists.append(a)

    # print("====================")
print(lists)
print(len(lists))

# ['03', '32', '28', '33', '18', '04', '30', '21', '14', '17', '12', '13', '02', '15', '07', '22', '24', '31', '10', '26', '08', '19', '11', '29', '16', '23', '25', '09']
