n=int(input())
s=input()

# 初期値
s2='b'

# 0手目で合っているかチェック
if s==s2 and n==1:
    print(0)
    exit()

idx=0 # N手目
while True:
    idx+=1
    t=idx%3
    # 文字列を編集していく
    if t==0:
        s2='b' + s2 + 'b'
    elif t==1:
        s2='a' + s2 + 'c'
    elif t==2:
        s2='c' + s2 + 'a'
    # 入力値と合致したら結果を表示して終了
    if s==s2:
        print(idx)
        exit()
    # 入力値より長くなってしまったら強制終了
    if len(s2) > n:
        print(-1)
        exit()