file = "./zuhe/zuhe_all.txt"
with open(file, 'r') as f:
    content = f.readlines()


for i in content:
    a = i.strip().replace("[", "").replace("]", "").split(",")
    ji = 1
    for b in a:
        #ji*=int(b)
        print(b)
        print(int(b.strip()))
    print("======================")