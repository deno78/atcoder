n = int(input())
map = {}
for i in range(1,n+1):
    a = int(input())
    # i番目のボタンを押すと、aに飛ぶ、という情報を連想配列に入れていく
    map[i] = a

c=0
p=1
# 位置0からスタートして、連想配列のvalue->keyをリンクして辿っていく
for i in range(n):
    if p==2:
        # 位置が2に辿り着いたら終了
        print(c)
        exit(0)
    # 次のボタンに進み、手数をインクリメント。
    p=map[p]
    c+=1
# 着かなかった場合は失敗(-1)
print("-1")
