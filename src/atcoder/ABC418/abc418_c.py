import bisect
n,q=map(int,input().split())
alist=list(map(int,input().split()))
alist.sort()
blist=[]
max_alist=max(alist)
blist=[]
alist2=[0]
wk=0
for a in alist:
    wk+=a
    alist2.append(wk)
print(alist2)
for i in range(q):
    blist.append(int(input()))
for b in blist:
    if max_alist<b:
        print(-1)
    else:
        idx=bisect.bisect(alist,b)
        a1=alist2[idx]
        a2=(b-1)*(n-idx)
        print("#",b,idx,a1,a2)
        print(a1+a2)
