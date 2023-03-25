n=int(input())
t,a=map(int,input().split())
hlist=list(map(int,input().split()))

# 初期値は最大値無限大、場所の位置は-1(どこでもない)を指定
m=float('INF')
y=-1

# 各地点について調べていく
for i in range(n):
    # 気温を求めて、絶対値を算出
    p=t-hlist[i]*0.006
    p2=abs(a-p)
    # 最低記録を更新していたら、その場所を更新していく
    if p2<m:
        m=p2
        y=i

print(y+1)