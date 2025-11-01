from bisect import bisect

def check(wk,x):
    if x==0:
        return wk[x+1]-wk[x]
    elif x==len(wk)-1:
        return wk[x]-wk[x-1]
    else:
        return min(wk[x+1]-wk[x],wk[x]-wk[x-1])

n=int(input())
xlist=list(map(int,input().split()))

ans=0
wk=[0]
for i in range(n):
    x=xlist[i]
    idx=bisect(wk,x)
    wk.insert(idx,x)
    if idx==0:
        ans+=abs(wk[1]-wk[0])
        ans+=check(wk,idx+1)
    elif idx==len(wk)-1:
        v1=abs(wk[-1]-wk[-2])
        v2=check(wk,idx-1)
        ans+=v1+v2
    else:
        v1=(wk[idx+1]-wk[idx-1])*2
        v2a=check(wk,idx+1)
        v2b=check(wk,idx)
        v2c=check(wk,idx-1)
#        print(i,idx,wk,v1,v2a,v2b,v2c)
        ans+=v2b+v2a+v2c-v1
    print(ans)

