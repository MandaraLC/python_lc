#1.先筛选出25码，再去掉包含kill3的数据，最后取交集
import os
file = "./shaixuan25/25shaixuan_data_110.txt"
with open(file, 'r') as f:
    content = f.readlines()
print(f"共{len(content)}条数据")
kill3list = []
kill3set = [('07', 5), ('20', 4), ('05', 4), ('22', 3), ('27', 3), ('23', 3), ('16', 3), ('04', 3), ('30', 3), ('13', 3), ('01', 3), ('24', 3), ('02', 2), ('09', 2), ('19', 2), ('11', 2), ('15', 2), ('26', 2), ('29', 2), ('12', 2), ('25', 1), ('33', 1), ('14', 1), ('18', 1), ('17', 1), ('32', 1), ('06', 1)]
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

#['07', '20', '05', '22', '27', '23', '16', '04', '30', '13', '01', '24', '02', '09',
# '19', '11', '15', '26', '29', '12', '25', '33', '14', '18', '17', '32', '06']
#03
