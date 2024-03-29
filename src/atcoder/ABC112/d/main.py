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

dlist=make_divisors(m)

ans=0
for d in dlist:
    cnt=m//d
    if cnt>=n:
        ans=max(ans,d)
print(ans)