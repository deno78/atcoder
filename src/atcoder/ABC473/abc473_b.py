n=int(input())
alist=list(map(int,input().split()))

adict={}
for a in alist:
    if a not in adict.keys():
        adict[a]=0
    adict[a]+=1
    adict[a]%=2

ans=0
for k,v in adict.items():
    ans+=k*v
print(ans)

