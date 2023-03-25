# TODO edit the code

# param
n,m = map(int,input().split())
xlist=list(map(int,input().split()))
cydic={}
for i in range(m):
    c,y=map(int,input().split())
    cydic[c]=y

# solve
dp=[]
for i in range(n+1):
    dp.append([-1]*(n+1))

dp[0][0]=0
for i in range(n):
    for j in range(n):
        if dp[i][j]!= -1:
            # 表がでたら、カウンタ＋１してボーナス計算
            if (j+1) in cydic.keys():
                dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+xlist[i] + cydic[j+1])
            else:
                dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+xlist[i])
    # 裏がでたら、次のステップのカウンタ0の金額を更新
    dp[i+1][0]=max(dp[i])


# answer
ans=max(dp[-1])
print(ans)