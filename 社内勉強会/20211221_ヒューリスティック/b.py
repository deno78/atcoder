# 入力値を受け取る
D=int(input())
C=list(map(int,input().split()))
S=[]
for i in range(D):
    S.append(list(map(int,input().split())))
T=[]
for i in range(D):
    T.append(int(input())-1)

m=0 # 満足度
L=[0]*26 # 最後に開催した日の記録
for d in range(D):
    t=T[d]
    s=S[d][t]
    m+=s
    L[t]=d+1
    for i in range(26):
        m-=(d+1-L[i])*C[i]
    print(m)
