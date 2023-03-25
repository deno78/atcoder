n=int(input())
alist=list(map(int,input().split()))

adic={}
for i in range(n):
    a=alist[i]
    if a not in adic.keys():
        adic[a]=[]
    adic[a].append(i)

ans=0
for k in adic.keys():
    a=len(adic[k])
    if k-1 in adic.keys():
        a+=len(adic[k-1])
    if k+1 in adic.keys():
        a+=len(adic[k+1])
    ans=max(a,ans)
print(ans)