file = open("list1_20190416_2.txt")
#file = open("../list.txt")
#f = open('new_result.txt', 'a')
f = open('list1_20190416_09.txt', 'a')

while 1:
    line = file.readline()
    #print(line)
    if ", 9" in line:
    #if ", 4," not in line:
        f.write(line)

    if not line:
        break
    pass
file.close()


#判断字符串内是否有子字符串
# zimu= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# zi= "45"
# result = zi in zimu
# print(result)