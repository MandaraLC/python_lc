thelist = []
for i in range(33):
    if i+1 < 10:
        thelist.append('0'+str(i+1))
    else:
        thelist.append(str(i+1))
print(thelist)