import math


lr=input().split()
l=int(lr[0])
r=int(lr[1])

# 全体を求める
total=(r-l+1)*(r-l+1)
print(total)

# x,yの片方を固定して、最大公約数
for x in range(l,r+1):
    t1=l//x
    t2=r//x
    print("{} {}-{}".format(x,t1,t2))
    total-=(t2-t1)

print(total)
