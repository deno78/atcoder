n,k=map(int,input().split())
llist=list(map(int,input().split()))

ans=0
llist.sort(reverse=True)

for i in range(k):
    ans+=llist[i]

print(ans)