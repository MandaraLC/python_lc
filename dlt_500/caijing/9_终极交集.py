#1.先筛选出25码，再去掉包含kill3的数据，最后取交集
import os
# file = "./shaixuan25/25shaixuan_data_110.txt"
# with open(file, 'r') as f:
#     content = f.readlines()
kill3list = []
kill3set = [('22', 5), ('04', 4), ('31', 3), ('17', 3), ('08', 3), ('26', 3), ('03', 3), ('05', 3), ('06', 3), ('19', 3), ('20', 3), ('21', 3), ('07', 2), ('10', 2), ('28', 2), ('27', 2), ('18', 2), ('09', 2), ('02', 2), ('12', 1), ('29', 1), ('14', 1), ('23', 1), ('01', 1), ('24', 1), ('33', 1), ('32', 1), ('30', 1), ('13', 1)]
for i in kill3set:
    kill3list.append(i[0])

print("排除的：", kill3list)

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
print("剩下的：", therest)
