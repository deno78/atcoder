h,w,n=map(int,input().split())

ab=[]
alist=[]
blist=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append([a,b])
    alist.append(a)
    blist.append(b)
alist=list(set(alist))
blist=list(set(blist))
alist.sort()
blist.sort()
adic={}
bdic={}

for i in range(len(alist)):
    adic[alist[i]]=i+1
for i in range(len(blist)):
    bdic[blist[i]]=i+1

for a,b in ab:
    a2=adic[a]
    b2=bdic[b]
    print("{} {}".format(a2,b2))