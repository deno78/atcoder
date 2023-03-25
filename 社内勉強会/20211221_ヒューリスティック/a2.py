def calc(T):
    v=0 # 満足度
    L=[0]*26 # 最後に開催した日の記録
    for d in range(D):
        t=T[d]
        s=S[d][t]
        v+=s
        L[t]=d+1
        for i in range(26):
            v-=(d+1-L[i])*C[i]
    return v

# 入力値を受け取る
D=int(input())
C=list(map(int,input().split()))
S=[]
for i in range(D):
    S.append(list(map(int,input().split())))

T=[]
# 試しにその日で一番大きい満足度のものを順に選んでいく手法で
for d in range(D):
    m=max(S[d])
    T.append(S[d].index(m))

print(calc(T))

for t in T:
    print(t+1)