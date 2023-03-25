kx = input('').split()
k=int(kx[0])
x=int(kx[1])

xs = []
# 数直線上のxから前後i(0-k)ずらしたリストを作る
for i in range(k):
    xs.append(x-i)
    xs.append(x+i)

# リストの重複を排除
xs=list(set(xs))
# リストをソート
xs.sort()

# 文字列に変換
xstr=[str(n) for n in xs]

# 文字列を半角空白で区切って表示
print(" ".join(xstr))