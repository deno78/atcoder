n = int(input())
plist=list(map(int,input().split()))
MAX_SCORE=100*n+1 # 最大取得点数
dp=[]
for _ in range(n+1):
    dp.append ([0]*MAX_SCORE)

dp[0][0]=1
for i in range(n):
    p=plist[i]
    for j in range(MAX_SCORE):
        if j-p>=0:
            dp[i+1][j]=dp[i][j]+dp[i][j-p]
        else:
            dp[i+1][j]=dp[i][j]

ans=0
for d in dp[n]:
    if d>0:
        ans+=1
print(ans)