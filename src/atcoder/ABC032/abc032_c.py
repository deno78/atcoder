nk = input('').split()
n = int(nk[0])
k = int(nk[1])

slist = []
for i in range(n):
    slist.append(int(input('')))

if 0 in slist:
    print(n)
    exit(0)

x=0 # 配列の長さ
r=0 # 右端
tmp=1 # 計算結果
for l in range(n):
    # まずrをできる限り大きくする
    while r < n and tmp*slist[r]<=k:
        tmp*=slist[r]
        r+=1
    # 解の判定
    x=max(x,r-l)
    # 次の左端を決める前の処理
    if l==r:
        # 左端が右端に追いついたら右端を1つインクリメント
        r+=1
    else:
        # 追いついていなかったら左端が1つ進むので、左端値で割る（短くする）
        tmp //=slist[l]
    print("len:{} ({}-{})".format(x,l,r))

print(x)