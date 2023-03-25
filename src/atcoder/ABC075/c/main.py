############################
#### Union Find テンプレ ####
############################
# 初期サイズszで親配列を作成する
def init_parents(sz):
    parents=[0]*sz
    # 初期値は自ノードとする
    for i in range(sz):
        parents[i]=i
    return parents

# ある要素の親を検索する
def find(parents,c):
    if parents[c]==c:
        # ある要素がルートならそれを返す
        return c
    else:
        # 親の親を調べる（再帰呼び出し！）
        p=find(parents,parents[c])
        # 調べる要素の親に親の親を設定する
        parents[c]=p
        return p

# ２つの要素を結合する
def unite(parents,a,b):
    # それぞれの親を探す
    pa=find(parents,a)
    pb=find(parents,b)
    # 親が異なる場合、一番上の親を更新する
    if pa!=pb:
        # インデクスの小さい方で大きい方を更新
        parents[max(pa,pb)]=min(pa,pb)

# ルート要素を取得する
def get_root(parents):
    return set(parents)
####################################
#### Union Find テンプレ ここまで
####################################

# 入力値を受け取る
nm=input().split()
n=int(nm[0])
m=int(nm[1])

ablist=[]
for i in range(m):
    a,b=map(int,input().split())
    ablist.append([a-1,b-1])

cnt=0
# 各辺について、調べる
for i in range(m):
    print("辺{}を削除する。".format(ablist[i]))
    print("[init] {}".format(parents))

    parents=init_parents(n)
    for j in range(m):
        # 調べる辺以外を結合していく
        if i!=j:
            a,b=ablist[j]
            unite(parents,a,b)
            print("[{}->{}] {}".format(a,b,parents))
    # もう一回全ノードについて調べなおす(圧縮しないと親の親まで遡れないため)
    for i in range(len(parents)):
        pi=find(parents,i)
    print("[ans ] {}".format(parents))
    # ルートノードの件数を調べて、2個以上なら分離するので、辺[i]は橋である
    if len(get_root(parents))>1:
        cnt+=1
print(cnt)