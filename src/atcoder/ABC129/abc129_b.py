n=int(input())
wlist=list(map(int,input().split()))

ans=float('INF')
for i in range(n):
    w1=sum(wlist[:i])
    w2=sum(wlist[i:])
    ans=min(ans,abs(w1-w2))
print(ans)