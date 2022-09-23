#1.先筛选出25码，再去掉包含kill3的数据，最后取交集
import os
file = "./shaixuan25/25shaixuan_data_110.txt"
with open(file, 'r') as f:
    content = f.readlines()
print(f"共{len(content)}条数据")
kill3list = []
kill3set = [('33', 6), ('27', 5), ('05', 4), ('20', 4), ('14', 3), ('25', 3), ('26', 3), ('31', 3), ('16', 3), ('21', 3)]
for i in kill3set:
    kill3list.append(i[0])

print(kill3list)

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

    print("====================")
print(lists)

