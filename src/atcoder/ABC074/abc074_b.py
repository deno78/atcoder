n=int(input())
k=int(input())
xlist=list(map(int,input().split()))

ans=0
for x in xlist:
    ans+=2*min(x,abs(x-k))

print(ans)