n=int(input())
alist=list(map(int,input().split()))

alist.sort()
MOD=998244353
dp=[]
for i in range(n+1):
    dp.append([0]*(n+1))

dp[0][0]=1
for i in range(n):
    a1=alist[i]
    for j in range(n):
        if alist[j]>=a1:
            dp[i+1][j]=dp[i][j-1] + dp[i][j]
    for d in dp:
        print(d)
    print("--------------------")
print(dp[n][n-1])