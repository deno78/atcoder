n,m=map(int,input().split())

ddict={}
cdict={}
for i in range(n):
    a,d,b=map(int,input().split())
    d-=1
    if d not in ddict:
        ddict[d]=[]
    ddict[d].append([a,b])
    if a not in cdict.keys():
        cdict[a]=0
    cdict[a]+=1

for d in range(m):
    if d in ddict.keys():
        for a,b in ddict[d]:
            cdict[a]-=1
            if cdict[a]==0:
                del cdict[a]
            if b not in cdict.keys():
                cdict[b]=0
            cdict[b]+=1
    print(len(cdict.keys()))

