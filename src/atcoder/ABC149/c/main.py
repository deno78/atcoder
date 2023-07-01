x=int(input())

# xの範囲である10**5+1桁までを調べる
n=10**6
###############################
# エラトステネスの篩テンプレ

# 値を配列番号で初期化する(1,2,3,4,5...)
p=[i for i in range(n+1)]
# 1は素数ではない
p[1]=0

# 調べる数は sqrt(n)+1まで
root_n=int(n**0.5)+1
# 2以上の数字について1個づつ調べていく
for i in range(1,root_n):
    # 配列の0は調べる対象外になっているためチェックしない
    if p[i] != 0:
        # iの倍数について、0にして消していく
        for j in range(i,int(n//i+1)):
            p[i*j]=0

# リスト上の重複する0を消すためにsetにして戻す。
plist=sorted(list(set(p)))
#print(plist)
###############################

# 素数リストを順に調べていってx以上のものを調べる
for i in plist:
    if i >= x:
        print(i)
        exit()