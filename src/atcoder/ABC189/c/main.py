n=int(input())
alist=list(map(int,input().split()))
ans=0
for l in range(n):
    x=alist[l]
    for r in range(l,n):
        x=min(x,alist[r])
        ans=max(ans,x*(r-l+1))

print(ans)

