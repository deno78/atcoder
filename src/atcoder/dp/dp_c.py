# TODO edit the code

# param
n = int(input())
abc=[]
for _ in range(n):
    abc.append(list(map(int,input().split())))

# A,B,Cそれぞれを選んだ場合の最大効用のリスト
dp=[]
for i in range(3):
    # 0日＋N日分を0で初期化
    dp.append([0]*(n+1))

# solve
# 初日は全て0で初期化
dp[0][0]=0
dp[1][0]=0
dp[2][0]=0

ans=0
# N日分調べていく
for i in range(n):
    # i+1日目にAを選ぶ場合、A[i] + （前日[B]か、前日[C]の大きい方）
    dp[0][i+1]=max(dp[1][i],dp[2][i])+abc[i][0]
    dp[1][i+1]=max(dp[0][i],dp[2][i])+abc[i][1]
    dp[2][i+1]=max(dp[0][i],dp[1][i])+abc[i][2]

ans=0
for d in dp:
#    print(d)
    ans=max(ans,d[-1])

# answer
print(ans)