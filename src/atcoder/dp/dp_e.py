# TODO edit the code

# param
n,w = map(int,input().split())

wv=[]
for _ in range(n):
    wv.append(list(map(int,input().split())))
dp=[]
for _ in range(n+1):
    dp.append([0]*w)

for i in range(n):
    w1=wv[i][0]
    v1=wv[i][1]
    # w-w1(i番目の品を持てない場合、前の項目をそのまま引き継ぐ)
    for j in range(w-w1,w):
        dp[i+1][j]=dp[i][j]
    for j in range(0,w-w1):
        dp[i+1][j]=max(dp[i+1][j],dp[i][j-w1]+v1)

# solve
ans = max(dp[-1])

# answer
print(ans)
