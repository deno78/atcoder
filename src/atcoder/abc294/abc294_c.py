n,m=map(int,input().split())

alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

clist=[]
clist.extend(alist)
clist.extend(blist)
clist.sort()

cdict={}
for i in range(len(clist)):
    c=clist[i]
    cdict[c]=i+1

ans=[]
for a in alist:
    ans.append(str(cdict[a]))
print(" ".join(ans))
ans=[]
for a in blist:
    ans.append(str(cdict[a]))
print(" ".join(ans))