# TODO edit the code

# param
n,m,k=map(int,input().split())

# solve
MOD=998244353

dp=[]
for i in range(n+1):
    dp.append([0]*(k+1))
for i in range(1,m+1):
    if i <=(k-n+1):
        dp[0][i]=1

for i in range(n):
    for j in range(1,k+1):
        for l in range(1,m+1):
            if j+l<=k:
                dp[i+1][j+l]=dp[i+1][j+l]+dp[i][j]
                dp[i+1][j+l]%=MOD


ans=sum(dp[-2])
print(ans%MOD)
