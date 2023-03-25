n,x,y,z=map(int,input().split())

alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

clist=[0]*n
adic={}
bdic={}
cdic={}
for i in range(n):
    a=alist[i]
    b=blist[i]
    c=a+b
    if a not in adic.keys():
        adic[a]=[]
    adic[a].append(i)
    if b not in bdic.keys():
        bdic[b]=[]
    bdic[b].append(i)
    if c not in cdic.keys():
        cdic[c]=[]
    cdic[c].append(i)

ans=[]
alist2=sorted(adic.keys(),reverse=True)
blist2=sorted(bdic.keys(),reverse=True)
clist2=sorted(cdic.keys(),reverse=True)
xc=0
yc=0
zc=0
for a in alist2:
    for j in adic[a]:
        if xc >= x:
            break
        ans.append(j)
        xc+=1
    if xc >= x:
        break
for b in blist2:
    for j in bdic[b]:
        if yc >= y:
            break
        if j not in ans:
            ans.append(j)
            yc+=1
    if yc >= y:
        break
for c in clist2:
    for j in sorted(cdic[c]):
        if zc >= z:
            break
        if j not in ans:
            ans.append(j)
            zc+=1
    if zc >= z:
        break
        
for a in sorted(ans):
    print(a+1)