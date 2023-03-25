n,k=map(int,input().split())
hlist=list(map(int,input().split()))

hlist.sort(reverse=True)
ans=0
for i in range(n):
    if i>=k:
        ans+=hlist[i]

print(ans)
