import copy
import random
import operator

#lst 要组合的列表  l 是几位数的组合
def combine(lst, l):
    result = []
    tmp = [0]*l
    length = len(lst)
    def next_num(li=0, ni=0):
        if ni == l:
            f = open('list1.txt', 'a')
            f.write("".join(str(copy.copy(tmp))))
            f.write('\n')
            result.append(copy.copy(tmp))
            return
        for lj in range(li,length):
            tmp[ni] = lst[lj]
            next_num(lj+1, ni+1)
    next_num()
    return result

ll = combine([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33], 6)
print(len(ll))
print(ll)