s=list(input())
t=list(input())

# @マークと置換可能な文字列
a=list('atcoder')

# 事前に置換可能な文字と判定するための連想配列を作っておく
# 2文字を判定するとき、足して11以上なら置換操作して同一にできる
w={}
for c in list('abcdefghijklmnopqrstuvwxyz@'):
    if c in a:
        w[c]=1
    elif c=='@':
        w[c]=10
    else:
        w[c]=0

for i in range(len(s)):
    if s[i] != t[i]:
        # 愚直に実装したケース.
#        if (s[i] in a and t[i]=='@') or (t[i] in a and s[i]=='@') :
        # 連想配列で計算を簡単にしたケース
        if w[s[i]]+w[t[i]]>10:
            pass
        else:
            # 1文字でも相違があれば終了
            print("You will lose")
            exit()

print("You can win")


