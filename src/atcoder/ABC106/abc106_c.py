s=input()
k=int(input())

# 5000兆日を定義しておく
d=5*10**15

# 1文字ずつ先頭から調べていく
for c in s:
    n = int(c)
    if n !=1: # 1は何乗しても1なので無視
        # 5000兆日まで進める
        for i in range(d):
            n=n*n # N乗していく
            if n>=k: # K文字目の範囲を越えたら捜索打ち切り
                # 結果を出力して終了
                print(c)
                exit()
    # 文字数を進める
    k=k-n
