n,x=map(int,input().split())
alist=list(map(int,input().split()))

ans=0
for i in range(n):
    if x>>i &1 == 1:
        ans+=alist[i]

print(ans)
