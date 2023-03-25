# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append([a,b])

# solve
dp=[]
for i in range(n+1):
    dp.append([0]*2)

dp[0][0]=1
dp[0][1]=1

MOD=998244353
for i in range(n-1):
    for j in range(2):
        for k in range(2):
            if ab[i+1][j]!=ab[i][k]:
                dp[i+1][j]=dp[i+1][j]+dp[i][k]
                dp[i+1][j]%=MOD

# answer
print(sum(dp[-2])%MOD)