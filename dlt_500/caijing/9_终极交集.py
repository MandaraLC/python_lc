#1.先筛选出25码，再去掉包含kill3的数据，最后取交集
import os
# file = "./shaixuan25/25shaixuan_data_110.txt"
# with open(file, 'r') as f:
#     content = f.readlines()
kill3list = []
kill3set = [('24', 5), ('31', 4), ('18', 4), ('23', 4), ('01', 3), ('15', 3), ('29', 3), ('26', 3), ('07', 3), ('12', 3), ('03', 3), ('20', 2), ('05', 2), ('32', 2), ('04', 2), ('27', 2), ('21', 2), ('06', 2), ('11', 1), ('22', 1), ('19', 1), ('17', 1), ('30', 1), ('16', 1), ('02', 1), ('33', 1), ('13', 1), ('09', 1), ('14', 1)]
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


# 排除的： ['24', '31', '18', '23', '01', '15', '29', '26', '07', '12', '03', '20', '05', '32', '04', '27', '21', '06', '11', '22', '19', '17', '30', '16', '02', '33', '13', '09', '14']
# 剩下的： ['08', '10', '25', '28']