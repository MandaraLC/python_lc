#1.先筛选出25码，再去掉包含kill3的数据，最后取交集
import os
# file = "./shaixuan25/25shaixuan_data_110.txt"
# with open(file, 'r') as f:
#     content = f.readlines()
kill3list = []
kill3set = [('27', 5), ('26', 5), ('01', 5), ('30', 3), ('33', 3), ('04', 3), ('10', 3), ('06', 3), ('28', 3), ('02', 3), ('20', 3), ('18', 3), ('23', 2), ('32', 2), ('24', 2), ('22', 2), ('17', 2), ('14', 2), ('16', 2), ('31', 1), ('13', 1), ('03', 1), ('11', 1), ('09', 1), ('07', 1), ('19', 1)]
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


# 排除的： ['27', '26', '01', '30', '33', '04', '10', '06', '28', '02', '20', '18', '23', '32', '24', '22', '17', '14', '16', '31', '13', '03', '11', '09', '07', '19']
# 剩下的： ['05', '08', '12', '15', '21', '25', '29']