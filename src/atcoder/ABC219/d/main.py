n=int(input())
x,y=map(int,input().split())
ablist=[]
mx=0
my=0
for i in range(n):
    a,b=map(int,input().split())
    ablist.append([a,b])
    mx+=a
    my+=b

inf = float("inf")
dp=[]
for i in range(n+1):
    dp.append([])
    for j in range(mx+1):
        dp[i].append([])
        for k in range(my+1):
            dp[i][j].append(inf)

dp[0][0][0] = 0

for i in range(n):
    a,b=ablist[i]
    for j in range(mx + 1):
        for k in range(my + 1):
            if a<=j and b<=k:
                j2=max(0,j-a)
                k2=max(0,k-b)
                dp[i + 1][j][k] = min(dp[i][j2][k2]+1, dp[i][j][k])
            else:
                dp[i + 1][j][k] = dp[i][j][k]

ans=inf
for j in range(x,mx):
    for k in range(y,my):
        ans=min(ans,dp[n][j][k])

if ans==inf:
    print(-1)
else:
    print(ans)
