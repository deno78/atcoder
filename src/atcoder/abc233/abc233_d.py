n,k = map(int,input().split())
alist=list(map(int,input().split()))

s=0
ddict={}
ddict[0]=[0]
for i in range(n):
    s+=alist[i]
    if s not in ddict.keys():
        ddict[s]=[]
    ddict[s].append(i)
ans=0
for a in alist:
    if (k-a) in ddict.keys():
        ans+=len(ddict[k-a])
print(ans)