n=int(input())
hlist=list(map(int,input().split()))

highest=-1
ans=0
for i in range(n):
    h=hlist[i]
    if h>=highest:
        highest=h
        ans+=1

print(ans)
