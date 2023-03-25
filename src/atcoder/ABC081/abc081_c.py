n,k=map(int,input().split())
alist=list(map(int,input().split()))
adict={}
for a in alist:
    if a not in adict.keys():
        adict[a]=0
    adict[a]+=1


adictlist=sorted(adict.items(),key=lambda x:x[1])

ans=0
for i in range(len(adictlist)-k):
    ans+=adictlist[i][1]

print(ans)
