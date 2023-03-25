# TODO edit the code

# param
n,w =map(int,input().split())
wv=[]
for _ in range(n):
    wv.append(list(map(int,input().split())))

dp=[]
for i in range(n+1):
    dp.append([0]*(w+1))

dp[0][0]=0

# solve
for i in range(n):      # 品分だけループ
    w2=wv[i][0]     # i番目の重さ
    v2=wv[i][1]     # i番目の価値
    for j in range(w+1):  # 各重さ分ループ
#        print("[{},{}] {} or {} + {}".format(i,j,dp[i][j],dp[i][j-w2],v2))
        if j-w2>=0:      # 品iを選ぶ前の状態の重さが存在していれば
            dp[i+1][j]=max(dp[i][j],dp[i][j-w2]+v2)
        else:
            dp[i+1][j]=dp[i][j]

ans=max(dp[-1])

# answer
print(ans)
