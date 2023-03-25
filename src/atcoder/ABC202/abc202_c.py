n=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
clist=list(map(int,input().split()))

amap={}
bcmap={}
for a in alist:
    if a in amap.keys():
        amap[a]+=1
    else:
        amap[a]=1

for i in range(n):
    c=clist[i]-1
    b=blist[c]
    if b in amap.keys():
        if b in bcmap.keys():
            bcmap[b]+=1
        else:
            bcmap[b]=1

cnt=0
for a,ac in amap.items():
    if a in bcmap.keys():
        bc=bcmap[a]
        cnt+=ac*bc
print(cnt)
