file = "shaixuankill3/kill3_shaixuan_data_108.txt"
with open(file, 'r') as f:
    content = f.readlines()

newlist = []
count = 0
for i in content:
    if count <= 5:
        slipt0 = i.strip().split(" ")
        slipt1 = slipt0[1].split(",")
        print(slipt1)
        for i in slipt1:
            #if i not in newlist:
            newlist.append(i)

        count+=1

print(newlist)
print(len(newlist))