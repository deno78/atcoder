s = input()
a=['A','G','C','T']
c=0 # 見つかった文字列長のカウンタ
m=0 # 文字列長の最大値
# 文字列の長さまでループ
for i in range(len(s)):
    if s[i] in a:
        c=c+1 # カウントアップ
        # 過去の最大値と比較して設定
        m=max(m,c)
    else:
        # AGCT以外ならカウンタを0に戻す
        c=0

print(m)
