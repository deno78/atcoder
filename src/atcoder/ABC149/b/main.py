# 正攻法でループしてシミュレーションするとタイムアウトする。
a,b,k = map(int,input().split())

print("{} {}".format(
    max(0,a-k),         # aからk枚食べた残り(最小0)
    max(0,b-max(0,k-a)) # bからk-aの残りを食べる(最小0)
    ))
