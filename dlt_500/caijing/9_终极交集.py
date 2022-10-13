#1.先筛选出25码，再去掉包含kill3的数据，最后取交集
import os
# file = "./shaixuan25/25shaixuan_data_110.txt"
# with open(file, 'r') as f:
#     content = f.readlines()
kill3list = []
kill3set = [('07', 5), ('29', 5), ('18', 4), ('08', 4), ('13', 3), ('21', 3), ('31', 3), ('02', 3), ('03', 3), ('01', 3), ('19', 2), ('16', 2), ('12', 2), ('15', 2), ('28', 2), ('04', 2), ('30', 1), ('27', 1), ('06', 1), ('33', 1), ('05', 1), ('23', 1), ('09', 1), ('17', 1), ('11', 1), ('25', 1), ('14', 1), ('10', 1), ('22', 1)]
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


# 排除的： ['07', '29', '18', '08', '13', '21', '31', '02', '03', '01', '19', '16', '12', '15', '28', '04', '30', '27', '06', '33', '05', '23', '09', '17', '11', '25', '14', '10', '22']
# 剩下的： ['20', '24', '26', '32']