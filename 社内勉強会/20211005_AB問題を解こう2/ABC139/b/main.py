a,b=map(int,input().split())
x=0
t=1
# 全体の口数が目的の数を超えるまでループ
while t<b:
    x+=1 # タップを1個追加する
    t=t+(a-1) # タップを1個追加すると口はa-1個増える
print(x)
