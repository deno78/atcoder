n=int(input())
alist=list(map(int, input().split()))

xdict={}
for a in alist:
    if a not in xdict.keys():
        xdict[a]=0
    xdict[a]+=1
klist=list(xdict.keys())
klist.sort(reverse=True)

wk=0
bdict={}
for i in range(len(klist)):
    k=klist[i]
    wk+=xdict[k]
    bdict[k]=wk
ans=0
for i in range(n+1):
    for k in klist:
        w=bdict[k]
        if w>=i and k>=i:
            ans=max(ans,i)
print(ans)