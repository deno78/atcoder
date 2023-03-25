n,m=map(int,input().split())
alist = list(map(int,input().split()))

# このコードでは速く終わるように得票順にソートしているが、しなくても間に合う
# 得票順にソート
alist.sort(reverse=True)

# 合計値を計算して、要求得票数を求める
s=sum(alist)
l=s/(4*m)

# 1個づつ票数の大きい方からM件までループ
for i in range(m):
    a=alist[i]
    # 表数が要求値を下回ったらNGとして終了
    if a<l:
        print('No')
        exit()

# m個、要求得票数を上回ったら成功
print('Yes')

