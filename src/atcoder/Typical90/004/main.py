h,w=map(int,input().split())

hwlist=[]
hlist=[0]*h
wlist=[0]*w

for i in range(h):
    a=list(map(int,input().split()))
    hwlist.append(a)
    hlist[i]=sum(a)
    for j in range(w):
        v=a[j]
        wlist[j]+=v

for i in range(h):
    l=[]
    for j in range(w):
        l.append (str(hlist[i]+wlist[j]-hwlist[i][j]))
    print(" ".join(l))