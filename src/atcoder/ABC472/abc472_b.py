n=int(input())
llist=list(map(int,input().split()))

all=sum(llist)

wk=0
ans=float("inf")

for i in range(n):
    wk+=llist[i]
    l2=all-wk
    ans=min(ans,abs(wk-l2))

print(ans)
