n=int(input())
alist=list(map(int,input().split()))

m=float('INF') # 回答する最小値

# 入力リストの最小から最大までの範囲内を全探索
for i in range(min(alist),max(alist)+1):
    # 算出したコストとそれまでの最小値を比較して代入
    cost=0
    for a in alist:
        cost+=(a-i)**2
    m=min(m,cost)

print(m)