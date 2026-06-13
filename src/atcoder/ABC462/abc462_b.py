n=int(input())
aklists=[]
for i in range(n):
    aklist=list(map(int,input().split()))
    aklists.append(aklist)

bdict={}
for i in range(n):
    bdict[i]=[]

for i in range(n):
    aklist=aklists[i]
    k=aklist[0]
    alist=aklist[1:]
    for a in alist:
        bdict[a-1].append(str(i+1))

for k,v in bdict.items():
    print(len(v)," ".join(v))
        