n,k=map(int,input().split())
alist=list(map(int,input().split()))

adict={}
for a in alist:
    if a not in adict.keys():
        adict[a]=0
    adict[a]+=1
bdict={}
for k,v in adict.items():
    if v not in bdict.keys():
        bdict[v]=0
    bdict[v]+=1
x=max(bdict.keys())
ans=bdict[x]
if x-1 in bdict.keys():
    ans+=bdict[x-1]
print(ans)