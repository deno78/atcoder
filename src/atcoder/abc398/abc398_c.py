n=int(input())
alist = list(map(int, input().split()))
d={}
kset=set([])
for i in range(n):
    a=alist[i]
    if a not in d.keys():
        d[a]=[]
        kset.add(a)
    else:
        if a in kset:
            kset.remove(a)
    d[a].append(i)

klist=list(kset)
klist.sort()

if len(klist)==0:
    print(-1)
else:
    print(d[max(klist)][0]+1)