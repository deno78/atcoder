n=int(input())

# 基本方針、全部足した数 - 足し忘れた数を求めて、

dic={} # キー乗数：値：約数のパターンを記録しておく連想配列
all=0 # 全部足したらいくつになるか、の数字

# 1から10まで足していく。
for i in range(1,10):
    for j in range(1,10):
        # 乗数を加算
        m=(i*j)
        all+=m
        # 乗数と約数組合せのパターンを連想配列に記録
        if m not in dic.keys():
            dic[m]=[]
        dic[m].append("{} x {}".format(i,j))

# 引数＝全部 - 足し忘れた数を計算
d=all-n
# 連想配列から目的の数字を取得して表示
for d in dic[d]:
    print(d)
