import math
# 組合せ数を求める計算関数
def combinations_count(n, r):
    if n==r:
        return 1
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n = int(input(''))

# 入力文字列をカウントする連想配列
sdict = {}
for i in range(n):
    # 入力文字列をソートしてキーにする
    s = "".join(sorted(input('')))
    if s in sdict.keys():
        # 外出文字ならカウントアップ
        sdict[s]+=1
    else:
        # 未出文字なら0で初期値設定
        sdict[s]=0
#    print("{} -> {}".format(s,sdict))

cnt=0
for v in sdict.values():
    # 出現した各要素について組合せを求める
    if v > 0:
        cnt+=combinations_count(v+1,2)

print(int(cnt))
