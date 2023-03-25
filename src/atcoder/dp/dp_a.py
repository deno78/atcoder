# TODO edit the code

# param
n = int(input())
hlist=list(map(int,input().split()))
INF=float('INF')

# solve
dp=[INF]*n #無限大で初期化する

dp[0]=0 #足場1にたどり着くコストは0

# 以下、足場がN個あるので、N-1までループ
for i in range(n-1):
    # 1歩進むのに必要なコストを計算
    c1=abs(hlist[i]-hlist[i+1])
    # 1歩進んだ先の累計コストをセット
    dp[i+1]=min(dp[i]+c1,dp[i+1])
    # 2歩進んだ時も同様
    if i+2<n: # 飛び越えなければ
        c2=abs(hlist[i+2]-hlist[i])
        dp[i+2]=min(dp[i]+c2,dp[i+2])
    print(dp)

# コストリストの一番最後の項目が結果
ans = dp[-1]

# answer
print(ans)
