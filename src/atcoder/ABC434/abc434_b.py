n,m=map(int,input().split())
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append((a,b))

abdict={}
for i in range(n):
    a,b=ab[i]
    if a not in abdict.keys():
        abdict[a]=[]
    abdict[a].append(b)

for i in range(1,m+1):
    blist=abdict[i]
    print(sum(blist)/len(blist))
