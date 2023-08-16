c=[]
for i in range(4):
    c.append(input().split())

for i in range(4):
    print("{} {} {} {}".format(c[3-i][3],c[3-i][2],c[3-i][1],c[3-i][0]))
    