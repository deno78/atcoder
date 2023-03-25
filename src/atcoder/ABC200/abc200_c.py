def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

n=int(input())
alist=list(map(int,input().split()))

bmap={}
for a in alist:
    key=a%200
    if key not in bmap.keys():
        bmap[key]=1
    else:
        bmap[key]=bmap[key]+1

cnt=0
for v in bmap.values():
    if v==2:
        cnt=cnt+1
    elif v > 2:
        a=cmb(v,2)
#        print("{} ->{}".format(v,a))
        cnt=cnt+a

print(int(cnt))