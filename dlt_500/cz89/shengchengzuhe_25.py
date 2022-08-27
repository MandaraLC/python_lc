import copy
# lst 要组合的列表  l 是几位数的组合
def combine(lst, l):
    result = []
    tmp = [0] * l
    length = len(lst)

    def next_num(li=0, ni=0):
        if ni == l:
            f = open('./list/list_all.txt', 'a')
            f.write("".join(str(copy.copy(tmp))))
            f.write('\n')
            result.append(copy.copy(tmp))
            return
        for lj in range(li, length):
            tmp[ni] = lst[lj]
            next_num(lj + 1, ni + 1)
    next_num()
    return result

file = "./shaixuan/shaixuan_data_098.txt"
with open(file, 'r') as f:
    content = f.readlines()

#177100*36=6375600
for i in content:
    slipt0 = i.strip().split(" ")
    slipt1 = slipt0[1].split(",")
    ll = combine(slipt1, 6)
    print(len(ll))

