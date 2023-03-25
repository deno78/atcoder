abx=input().split()
a=int(abx[0])
b=int(abx[1])
x=int(abx[2])

# 検索対象の範囲を左端と右端に設定
# 左端が条件を満たす、想定する最小値
left=0
# 右端が条件を満たさない、想定する最大値
right=10**9+1

# 左端と右端の幅が1になるまで繰返し
while left + 1 < right:

    # 真ん中の値＝金額を求める。
    mid=(left + right)//2
    val=a*mid+len(str(mid))*b
    print("left:{} mid:{} right:{}".format(left,mid,right))
    # 金額が所持金より少なければ左端を次の中央値にシフト
    if val <=x:
        left = mid
    else:
        # 所持金を越えていたら右端を次の中央値にシフト
        right = mid

print(left)

