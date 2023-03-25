# TODO edit the code

# param
n,k = map(int,input().split())
hlist=list(map(int,input().split()))
INF=float('INF')

# solve
dp=[INF]*n

# 足場1にたどり着くコストは0
dp[0]=0

# 2～Nまでの足場を調べていく
for i in range(n-1):
    # １～Kまで飛ぶ先について調べる
    for j in range(k):
        idx=i+j+1 # 調べる先のインデクス
        if idx <n: # 調べるリストを越えていなければ判定
            c=abs(hlist[i]-hlist[idx]) # コスト計算
            dp[idx]=min(dp[i]+c,dp[idx]) # 計算したコストと小さい方

# コストリストの一番最後の項目が結果
ans = dp[-1]

# answer
print(ans)
