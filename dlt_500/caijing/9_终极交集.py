#1.先筛选出25码，再去掉包含kill3的数据，最后取交集
import os
file = "./shaixuan25/25shaixuan_data_110.txt"
with open(file, 'r') as f:
    content = f.readlines()
# print(f"共{len(content)}条数据")
kill3list = []
kill3set = [('11', 5), ('31', 4), ('01', 4), ('28', 4), ('15', 3), ('25', 3), ('06', 3), ('12', 3), ('19', 3), ('29', 3), ('05', 2), ('07', 2), ('02', 2), ('21', 2), ('16', 2), ('30', 2), ('33', 2), ('32', 2), ('03', 2), ('09', 2), ('14', 2), ('18', 1), ('10', 1), ('17', 1), ('20', 1), ('24', 1), ('04', 1)]
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