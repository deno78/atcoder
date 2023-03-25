from itertools import groupby

n=int(input())
hlist=list(map(int,input().split()))
m=max(hlist)
hmap=[]
for i in range(m):
    hmap.append([0]*n)
    for j in range(n):
        if hlist[j]>i:
            hmap[i][j]=1

ans=0
for i in range(m):
    l=hmap[i]
    a=0
    print(l)
    for k,v in groupby(l):
        if k==1:
            a+=1
    ans+=a
print(ans)