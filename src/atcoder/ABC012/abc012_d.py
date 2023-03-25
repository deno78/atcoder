# ワーシャルフロイド
def warshall_floyd(v,dmap):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                pre=dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                if pre!=dist[i][j]:
                    for x in range(v):
                        line=""
                        for y in range(v):
                            if x==i and y==j:
                                line+= "[" + str(dist[x][y]) + "]"
                            else:
                                line+= " " + str(dist[x][y]) + " "

nm = input().split()
n = int(nm[0])
m = int(nm[1])

# 距離リストを初期化
dist = [[float("inf")] * (n) for i in range(n)]

# 入力値を距離リストに反映
for i in range(m):
    abt=list(map(int,input().split()))
    a=abt[0]
    b=abt[1]
    t=abt[2]
    dist[a-1][b-1]=t
    dist[b-1][a-1]=t

# ワーシャルフロイドでリストを修正
warshall_floyd(n,dist)

# 距離リストの中で最小値を取得
min_d=float("inf")
for d in dist:
    min_d=min(min_d,max(d))
print(min_d)
