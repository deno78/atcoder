import bisect
n,l,r=map(int,input().split())
s=input()

sdict={}
for i in range(n):
    c=s[i]
    if c not in sdict:
        sdict[c]=[]
    sdict[c].append(i)

ans=0
for c,idxs in sdict.items():
    idxs.sort()
    for p in idxs:
        left=bisect.bisect_left(idxs,p+l)
        right=bisect.bisect_right(idxs,p+r)
        ans+=right-left

print(ans)
