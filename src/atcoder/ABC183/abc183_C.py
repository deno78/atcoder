import itertools

nk = input('').split()
n = int(nk[0])
k = int(nk[1])

tlist = []
for i in range(n):
    t = list(map(int,input('').split()))
    tlist.append(t)


cnt=0
for v in itertools.permutations(list(range(2,n+1)),n-1):
    d = 0
    e1=1
    for e2 in v:
        d+=tlist[e1-1][e2-1]
        e1 = e2
    d+=tlist[e2-1][0]
#    print("[{}] -> {}".format(v,d))
    if d == k:
        cnt+=1

print(cnt)

