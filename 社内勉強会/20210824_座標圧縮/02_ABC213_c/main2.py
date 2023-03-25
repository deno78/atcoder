h,w,n=map(int,input().split())

ab=[] # 元の入力値ペア
alist=[] # 縦についてのリスト
blist=[] # 横についてのリスト
for i in range(n):
    a,b=map(int,input().split())
    ab.append([a,b])
    alist.append(a)
    blist.append(b)

# 元リストを重複排除してソートしたリストを作る
alist=list(set(alist))
blist=list(set(blist))
alist.sort()
blist.sort()

# ソート済み＆重複排除したリストに順位を付けて値＆順位の連想配列に格納
adic={}
bdic={}
for i in range(len(alist)):
    adic[alist[i]]=i+1
for i in range(len(blist)):
    bdic[blist[i]]=i+1

# 値＆順位の連想配列を調べながら表示していく
for a,b in ab:
    a2=adic[a]
    b2=bdic[b]
    print("{} {}".format(a2,b2))