n,l=map(int,input().split())
dlist=list(map(int, input().split()))

ddict={}
p=0
ddict[0]=1
for i in range(n-1):
    d=dlist[i]
    p+=d
    p%=l
    if p not in ddict.keys():
        ddict[p]=0
    ddict[p]+=1

alist=list(ddict.keys())
alist.sort()

ans=0
for i in range(len(alist)):
        a1=alist[i]
        d=l//3
        a2=a1+d
        a3=a2+d
#            print("[{} {}] a1={} a2={} a3={} d1={} d2={} d3={}".format(i,j,a1, a2, a3,d1, d2, d3))
        if a2 in ddict.keys() and a3 in ddict.keys():
            c1=ddict[a1]
            c2=ddict[a2]
            c3=ddict[a3]
            ans+=(c1*c2*c3)
print(ans)
