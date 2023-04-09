c=[]
for i in range(3):
    c.append(list(map(int,input().split())))


for a1 in range(0,101):
    a2=c[1][0]-c[0][0]+a1
    a3=c[2][0]-c[0][0]+a1
    for b1 in range(0,101):
        b2=c[0][1]-c[0][0]+b1
        b3=c[0][2]-c[0][0]+b1
        a=[a1,a2,a3]
        b=[b1,b2,b3]
        ok=True
        for i in range(3):
            for j in range(3):
                if c[i][j]!=a[i]+b[j]:
#                    print("[{},{}] {}+{}={}".format(i,j,a[i],b[j],c[i][j]))
                    ok=False
        if ok==True:
            print("Yes")
            exit()

print("No")


