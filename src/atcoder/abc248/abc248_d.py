# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))
q=int(input())
qlist=[]
xlist=[]
for i in range(q):
    x=list(map(int,input().split()))
    qlist.append(x)
    xlist.append(x[2])

alist2=[]
for i in range(n):
    map={}
    for x in xlist:
        if x not in map.keys():
            map[x]=0
    alist2.append(map)

for i in range(n):
    a=alist[i]
    for k,v in alist2[i].items():
        alist2[i+1][k]=v
    alist2[i][a]+=1


print(alist2)
for l,r,x in qlist:
    j=xlist.index(x)
    print(alist2[r-1][j]-alist2[l-1][j])
