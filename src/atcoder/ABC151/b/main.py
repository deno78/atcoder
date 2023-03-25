n,k,m=map(int,input().split())

alist=list(map(int,input().split()))

x=m*n - sum(alist)
if x<=k:
    print(max(x,0))
else:
    print(-1)
