n=int(input())
alist=list(map(int,input().split()))

adict={}
for i in range(n):
    a=alist[i]
    if a not in adict.keys():
        adict[a]=[]
    adict[a].append(i)

ans=0
for key in adict.keys():
    blist=adict[key]
    l=len(blist)
    if l>=2:
        wk=l*(l-1)//2*(n-l)
        ans+=wk

print(ans)

