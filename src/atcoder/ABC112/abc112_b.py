N,T=map(int,input().split())
ans=float('INF')
for i in range(N):
    c,t=map(int,input().split())
    if t<=T:
        ans=min(ans,c)
if ans != float('INF'):
    print(ans)
else:
    print('TLE')
