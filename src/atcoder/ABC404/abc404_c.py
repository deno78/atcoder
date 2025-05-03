n,m=map(int,input().split())
ab=[]
abdict={}
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    ab.append([a,b])
    if a not in abdict.keys():
        abdict[a]=[]
    abdict[a].append(b)
    if b not in abdict.keys():
        abdict[b]=[]
    abdict[b].append(a)

r=[0]*n
r2=[0]*n
for i in range(m):
    a,b=ab[i]
    r[a]+=1
    r[b]+=1

for i in range(n):
    if r[i]!=2:
        print("No")
        exit()

wk=[]
wk.append(0)
while len(wk)>0:
    w=wk.pop(0)
    for v in abdict[w]:
        if r2[v]==0:
            wk.append(v)
            r2[v]=1

for x in r2:
    if x==0:
        print("No")
        exit()

print("Yes")