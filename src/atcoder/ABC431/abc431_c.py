from bisect import bisect_left, bisect_right
n,m,k=map(int,input().split())
hlist=list(map(int,input().split()))
blist=list(map(int,input().split()))
hlist.sort()
blist.sort()
ans=0
l=0
r=len(blist)-1
for i in range(n):
    if l>r:
        break
    h=hlist[i]
    if blist[r]==h:
        ans+=1
        r-=1
    else:
        idx=bisect_left(blist, h, lo=l, hi=r+1)
        if idx<=r:
            ans+=1
            l=idx+1

if ans >= k:
    print("Yes")
else:
    print("No")