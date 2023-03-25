n,q=map(int,input().split())
ab={}

for i in range(q):
    t,a,b=map(int,input().split())
    if t == 1:
        if a not in ab.keys():
            ab[a]=set([])
        ab[a].add(b)
    elif t == 2:
        if a in ab.keys() and b in ab[a]:
            ab[a].remove(b)
    elif t == 3:
        if a in ab.keys() and b in ab.keys() and b in ab[a] and a in ab[b]:
            print("Yes")
        else:
            print("No")
