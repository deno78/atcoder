n=int(input())

clist=[]
for i in range(1,7):
    clist.append(str(i))

n=n%30

for i in range(n):
    i1=i%5
    i2=i%5+1
    w1=clist[i1]
    w2=clist[i2]
    clist[i1]=w2
    clist[i2]=w1
    #print("[{}] {}".format(i,clist))

print("".join(clist))

