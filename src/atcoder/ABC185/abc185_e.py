nm = input('').split()
n=int(nm[0])
m=int(nm[1])

alist=list(map(int,input('').split()))
blist=list(map(int,input('').split()))

d = [[0]*(len(alist)+1)]*(len(blist)+1)

for i in range(len(blist)):
    for j in range(len(alist)):
        print("[{},{}] a:{} b:{}".format(i,j,alist[j],blist[i]))
        if alist[j] == blist[i]:
            d[i+1][j+1] == d[i][j]
            d[i+1][j]=d[i][j]
            d[i][j+1]=d[i][j]
        else:
            d[i+1][j]=d[i][j]+1
            d[i][j+1]=d[i][j]+1
    for dx in d:
        print(dx)

