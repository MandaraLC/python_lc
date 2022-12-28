'''
000-999
'''
alllist = []
for i in range(1000):
    if i < 10:
        i = '00'+str(i)
    elif i >= 10 and i < 100:
        i = '0' + str(i)
    else:
        i = str(i)

    alllist.append(list(map(int, list(i))))

print(f"总列表，共{len(alllist)}", alllist)

hezhi = []
for a in alllist:
    he0 = 0
    for b in a:
        he0+=int(b)
    hezhi.append(he0)
print(f"和值，共{len(hezhi)}", hezhi)
print(f"和值，共{len(list(set(hezhi)))}", list(set(hezhi)))
print("1000/28="+str(1000/28))
