n=int(input())
plist=list(map(int,input().split()))

r=1
qlist=[-1]*n
pdict={}
for i in range(n):
    p=plist[i]
    if p not in pdict.keys():
        pdict[p]=[]
    pdict[p].append(i)

klist=list(pdict.keys())
klist.sort(reverse=True)
r=1
for k in klist:
    for i in pdict[k]:
        qlist[i]=r
    r+=len(pdict[k])

for i in range(n):
    print(qlist[i])