from bisect import bisect_left,bisect_right

n,m,c=map(int,input().split())
alist=list(map(int,input().split()))

adict={}
for i in range(n):
    a=alist[i]
    if a not in adict.keys():
        adict[a]=0
    adict[a]+=1

akeys=sorted(adict.keys())
akeylen=len(akeys)
bdict={}
b1=akeys[0]
for i in range(1,akeylen):
    a1=akeys[i-1]
    a2=akeys[i]
    bdict[i]=(a2-a1)
if i>1:
    bdict[i+1]=m-a2
else:
    bdict[1]=m
#print(bdict)

ans=0
idx1=0
for i in range(akeylen):
    idx2=i
    a=akeys[(i+1)%akeylen]
    if i==0:
        a0=0
    else:
        a0=akeys[i]
    wk=0
    while wk<c:
        idx2+=1
        idx2%=akeylen
        wk+=adict[akeys[idx2]]
#        print("##",a,idx2,akeys[idx2],wk)
    if idx2==0:
        idx2=akeylen        
    ans+=wk*bdict[idx2]
#    print("**",a,idx1,idx2,a,a0,wk,ans)
    idx1=idx2+1
    idx1%=akeylen
print(ans)