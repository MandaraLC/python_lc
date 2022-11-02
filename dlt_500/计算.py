file = "./data/data_ssq.txt"
with open(file, 'r') as f:
    content = f.readlines()

for data in content:
    split = data.strip().split(" ")
    print(split)
    #取和
    he0_1 = int(split[0]) + int(split[1])
    he0_2 = int(split[0]) + int(split[2])
    he0_3 = int(split[0]) + int(split[3])
    he0_4 = int(split[0]) + int(split[4])
    he0_5 = int(split[0]) + int(split[5])

    he1_2 = int(split[1]) + int(split[2])
    he1_3 = int(split[1]) + int(split[3])
    he1_4 = int(split[1]) + int(split[4])
    he1_5 = int(split[1]) + int(split[5])

    he2_3 = int(split[2]) + int(split[3])
    he2_4 = int(split[2]) + int(split[4])
    he2_5 = int(split[2]) + int(split[5])

    he3_4 = int(split[3]) + int(split[4])
    he3_5 = int(split[3]) + int(split[5])

    he4_5 = int(split[4]) + int(split[5])
    print(f"和值：{he0_1} {he0_2} {he0_3} {he0_4} {he0_5} {he1_2} {he1_3} {he1_4} "
          f"{he1_5} {he2_3} {he2_4} {he2_5} {he3_4} {he3_5} {he4_5}")

    print("=====================================================================")











