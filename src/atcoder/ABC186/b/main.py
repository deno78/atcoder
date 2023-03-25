hw=list(map(int,input().split()))

alist=[]
for i in range(hw[0]):
    alist.append(list(map(int,input().split())))

d=0
b=float('INF')
for a1 in alist:
    for a in a1:
        b=min(b,a)
for a1 in alist:
    for a in a1:
        d+=(a-b)

print(d)