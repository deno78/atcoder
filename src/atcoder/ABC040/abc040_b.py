n=int(input())

ans=float('INF')

for h in range(1,int(n**0.5)+1):
    w=n//h
    x=n-h*w
    ans=min(ans,abs(h-w)+x)
print(ans)