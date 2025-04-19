n,m=map(int,input().split())
klist=[]
for i in range(m):
    klist.append(list(map(int,input().split())))

blist=list(map(int,input().split()))

bdict={}
for i in range(n):
    bdict[i+1]=[]

clist=[]
for i in range(m):
    k=klist[i][0]
    clist.append(k)
    alist=klist[i][1:]
    for a in alist:
        bdict[a].append(i)
ans=0
for i in range(n):
    b=blist[i]
    for v in bdict[b]:
        clist[v]-=1
        if clist[v]==0:
            ans+=1
    print(ans)

