s=input()
k=int(input())

# 文字列SをK文字目まで検索する
for c in s[:k]:
    # 1個でも1以外の文字列があればそれを出力して終了
    if c!='1':
        print(c)
        exit()

# 上記以外、K文字目まで1個も見つからなければ1を出力
print('1')