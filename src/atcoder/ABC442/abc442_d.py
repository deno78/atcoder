n,q=map(int,input().split())
alist=list(map(int,input().split()))
queries=[]
for _ in range(q):
    queries.append(list(map(int,input().split())))

blist=[]
wk=0
for i in range(n):
    wk+=alist[i]
    blist.append(wk)

for q in queries:
    if q[0]==1:
        x=q[1]-1
        if 0<=x<n-1:
            a=alist[x]
            b=alist[x+1]
            base=blist[x-1] if x>0 else 0
            blist[x]=base+b
            blist[x+1]=blist[x]+a
            alist[x],alist[x+1]=b,a
    elif q[0]==2:
        l=q[1]-1
        r=q[2]-1
        print(blist[r]-(blist[l-1] if l>0 else 0))

