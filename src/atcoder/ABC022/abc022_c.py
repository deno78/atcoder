# ワーシャルフロイド法の参考アルゴリズム

def print_d():
    print("----------------------")
    for i in range(n):
        line=""
        for j in range(n):
            line += " " + str(d[i][j]) + " \t"
        print(line)
    print("----------------------")

def print_d2(a,b,c):
    print("--- i={},j={},k={} ---".format(a,b,c))
    for i in range(n):
        line=""
        for j in range(n):
            if (i,j) in [(a,c),(c,b)]:
                line += "|" + str(d[i][j]) + "|\t"
            elif (i,j) in [(a,b)]:
                line += "[" + str(d[i][j]) + "]\t"
            else:
                line += " " + str(d[i][j]) + " \t"
        print(line)
    print("----------------------")

nm = input().split()
n=int(nm[0])
m=int(nm[1])

# 家の間の2次元マトリクスを作る(n x n)
d=[]
# 初期の移動コストは全て無限大とする
for i in range(n):
    d.append([float('inf')]*n)

# 入力値から条件となる移動コストを埋めていく
for i in range(m):
    uvl=input().split()
    u=int(uvl[0])-1
    v=int(uvl[1])-1
    l=int(uvl[2])
    d[u][v]=l
    d[v][u]=l

print_d() # 埋める前の状態表示
# ワーシャルフロイドで最短移動時間を埋めてみる。
for i in range(n):         # 始点
    for j in range(n):     # 終点
        for k in range(n): # 中継地点
            # 始点i -> 終点jが同一の場合は計算せず除外
            if i!=j:
                # 家１へ2度の出入りはしないので家[0]は除外
                if i!=0 and j!=0 and k != 0:
                    # それ以外の家の間での3点間での最短移動時間を埋めていく
                    d1 = d[i][j]                      # 補正前移動コスト
                    d2 = min(d[i][j],d[i][k]+d[k][j]) # 補正後移動コスト
                    # i->jの間の移動時間を、i->jか、i->k->jの短い方で補正する
                    d[i][j] = min(d[i][j],d[i][k]+d[k][j])
                    # 結果が変わる場合、ログ出力する
                    if d1 != d2 :
                        print_d2(i,j,k)
                        input()

print_d() # 埋めた後の状態表示

# 全部の組合せで0からどこか1件と、どこか1件から0の距離を求める
ans=float('inf')
for i in range(n):
    for j in range(n):
        if i!=j:
            t=d[0][i] + d[i][j] + d[j][0]
            if t!= float('inf'):
                print("From:0->{}[{}]\tTransit:{}->{}[{}]\tTO:{}->0[{}]\t=> Total:{}".format(i,d[0][i],i,j,d[i][j],j,d[j][0],t))
            # 最短経路を選ぶ
            ans=min(ans,t)

if ans== float('inf'):
    print(-1)
else:
    print(ans)
