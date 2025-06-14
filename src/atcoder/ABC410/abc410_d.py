n,m=map(int,input().split())
abw=[]
abdict={}
wmap=[]
cmap=[]
for i in range(n):
    wmap.append([-1]*n)
    cmap.append([-1]*n)
    abdict[i]=[]

for i in range(m):
    a,b,w=map(int, input().split())
    a-=1
    b-=1
    abdict[a].append(b)
    abdict[b].append(a)
    wmap[a][b]=w
    wmap[b][a]=w
    cmap[a][b]=i
    cmap[b][a]=i

clist=[0]*m
wk=[]
wk.append([0,0,clist])
aset=set([])
while len(wk)>0:
    w=wk.pop(0)
    p=w[0]
    c=w[1]
    s=w[2]
#    print("{} {} {}".format(p, c, s))
    for b in abdict[p]:
        c2=c^wmap[p][b]
        r=cmap[p][b]
        if b==n-1:
            if c2 not in aset:
                aset.add(c2)
                wk.append([b,c2,s.union(set([b]))])
        elif b not in s:
            wk.append([b,c2,s.union(set([b]))])

if len(aset)==0:
    print(-1)
else:
    print(min(aset))
