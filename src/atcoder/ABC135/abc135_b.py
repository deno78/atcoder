n = int(input(''))
plist = list(map(int,input('').split()))

# インデクスと実際の値を調べていく
err_idx=[] # 差異がある場合のインデクス
err_val=[] # 差異がある場合の実値
for i in range(n):
    p = plist[i]
    # 正常であれば、インデクス＋１＝実値のはず
    if p != i+1:
        # 違ったら記録
        err_idx.append(i+1)
        err_val.append(p)

# 2つ以上差異があったらNG
if len(err_idx) > 2:
    print('NO')
elif len(err_idx)==2:
    # 差異が2つちょうどで、ソートしたら同じになるかチェック
    err_idx.sort()
    err_val.sort()
    if err_idx[0] == err_val[0] and err_idx[1] == err_val[1]:
        print('YES')
    else:
        print('NO')
else:
    # エラー件数が0件なら問題無し
    print('YES')
