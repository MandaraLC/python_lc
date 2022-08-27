import copy    #实现list的深复制
import random
import operator
#dlt
#35的阶乘 除以 （5的阶乘*30的阶乘）
#38955840/120 = 324632

#12的阶乘 除以 （2的阶乘*10的阶乘）
#132/2 = 66
#共 324632 * 66 = 21425712 组合方式

#ssq
# 33 16
# 6 1
# 33的阶乘 除以 （6的阶乘*27的阶乘）

#797448960/720 = 1107568*16 = 17721088


#lst 要组合的列表  l 是几位数的组合
def combine(lst, l):
    result = []
    tmp = [0]*l
    length = len(lst)
    def next_num(li=0, ni=0):
        if ni == l:
            result.append(copy.copy(tmp))
            return
        for lj in range(li,length):
            tmp[ni] = lst[lj]
            next_num(lj+1, ni+1)
    next_num()
    return result

ll = combine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2)
print(ll)

list3 = [6, 11]
for i in ll:
    if operator.eq(list3, i):
        print(i, "下标为：",ll.index(i))

for i in range(10000):
    newlist2 = combine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2)
    l = random.choice(newlist2)
    list = [6, 12]

    # newlist2 = combine([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], 5)
    # l = random.choice(newlist2)
    if operator.eq(list, l):
        print(random.choice(newlist2))
        break