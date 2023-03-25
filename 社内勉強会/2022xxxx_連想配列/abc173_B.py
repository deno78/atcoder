n = int(input(''))

# 入力文字列の一覧
l=['AC','WA','TLE','RE']

# 入力文字列毎の連想配列を用意しておく
d={}
for a in l:
    d[a]=0

# 入力文字列毎に該当する件数を１増やす
for i in range(n):
    s = input('')
    d[s]+=1

# 答えを表示
for a in l:
    print('{} x {}'.format(a,d[a]))
