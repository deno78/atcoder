def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

n,m=map(int,input().split())

# mの約数リストを作る
dlist=make_divisors(m)

ans=0
# それぞれの約数を調べて、
# alistの数がN個以上になるものを調べる。
for d in dlist:
    cnt=m//d # 多分最小値である(1+1+1+...)*nの数
    if cnt>=n:
        # 調べた数の中で最大値を記録しておく
        ans=max(ans,d)
print(ans)
