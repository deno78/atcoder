# 入力値の受取
D=int(input())
C=list(map(int,input().split()))
S=[]
for i in range(D):
    S.append(list(map(int,input().split())))
T=[]
for i in range(D):
    T.append(int(input())-1)

# 補正クエリの追加
M=int(input())
DQ=[]
for i in range(M):
    DQ.append(list(map(int,input().split())))

# 各補正クエリ毎に結果を計算していく
for dq in DQ:
    # 補正値
    d2 =dq[0]-1
    q=dq[1]-1

    v=0 # 満足度
    L=[0]*26 # 最後に開催した日の記録
    for d in range(D):
        # 補正をかける
        if d==d2:
            T[d]=q
        t=T[d]
        s=S[d][t]
        v+=s
        L[t]=d+1
        for i in range(26):
            v-=(d+1-L[i])*C[i]
    print(v)
