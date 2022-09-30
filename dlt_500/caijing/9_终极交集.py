#1.先筛选出25码，再去掉包含kill3的数据，最后取交集
import os
file = "./shaixuan25/25shaixuan_data_110.txt"
with open(file, 'r') as f:
    content = f.readlines()
# print(f"共{len(content)}条数据")
kill3list = []
kill3set = [('03', 4), ('32', 4), ('28', 4), ('33', 4), ('18', 3), ('04', 3), ('30', 3), ('21', 3), ('14', 3), ('17', 3), ('12', 2), ('13', 2), ('02', 2), ('15', 2), ('07', 2), ('22', 2), ('24', 2), ('31', 2), ('10', 2), ('26', 1), ('08', 1), ('19', 1), ('11', 1), ('29', 1), ('16', 1), ('23', 1), ('25', 1), ('09', 1)]
for i in kill3set:
    kill3list.append(i[0])

print(kill3list)

thelist33 = []
for i in range(33):
    if i+1 < 10:
        thelist33.append('0'+str(i+1))
    else:
        thelist33.append(str(i+1))

therest = []
for t in thelist33:
    if t not in kill3list:
        therest.append(t)
print(therest)