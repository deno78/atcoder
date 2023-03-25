# ユークリッドの互除法
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n=int(input())

alist=list(map(int,input().split()))

# 1番目と2番目以降の最大公約数を調べていく
m=alist[0]
for i in range(1,n):
    m=gcd(m,alist[i])

print(m)