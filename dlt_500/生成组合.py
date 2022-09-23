import copy
# lst 要组合的列表  l 是几位数的组合
def combine(lst, l):
    result = []
    tmp = [0] * l
    length = len(lst)

    def next_num(li=0, ni=0):
        if ni == l:
            f = open('./zuhe/zuhe_47——6.txt', 'a')
            f.write("".join(str(copy.copy(tmp))))
            f.write('\n')
            result.append(copy.copy(tmp))
            return
        for lj in range(li, length):
            tmp[ni] = lst[lj]
            next_num(lj + 1, ni + 1)
    next_num()
    return result

#生成1-33的列表
list1_33 = list(range(1, 34))
new_list = []
for i in list1_33:
    if i < 10:
        i = str("0"+str(i))
    new_list.append(str(i))
print(new_list)

#生成组合，共1107568种组合
ll = combine(new_list, 6)
print(len(ll))