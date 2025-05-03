n,m=map(int,input().split())
clist=list( map(int,input().split()))
alists=[]
for i in range(m):
    alist=list(map(int, input().split()))
    k=alist[0]
    alists.append(alist)
adict={}
for i in range(m):
    alist=alists[i]
    for a in alist[1:]:
        a-=1
        if a not in adict.keys():
            adict[a]=[]
        adict[a].append(i)
