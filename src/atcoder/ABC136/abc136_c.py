# 入力値を取得
n = int(input(''))
hlist = list(map(int,input('').split()))

# high water mark=現時点で一番高いラインを設定
hwm=hlist[0]
# リストの0を飛ばして、1から最後までをチェック
for i in range(1,len(hlist)):
#    print("[{}] {} - {}".format(i,hlist[i],hlist[i-1]))
    # hwmに1足しても届かない場合は、変更不可
    if hlist[i] - hwm < -1:
        print('No')
        exit(0)
    else:
        # 届く場合はhwmを更新して次へ
        hwm=max(hlist[i],hwm)

# ここまで来たら一回もNoでexitしてないはずなのでYes
print('Yes')