import sys
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

# 全部同じのを選んだらどうなるか
v=0
k=0
for i in range(26):
    T=[i]*D
    v2=calc(T)
    if v2>v:
        k=i
        v=v2
for d in range(D):
    print(k+1)
