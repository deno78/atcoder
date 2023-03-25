a,b=map(int,input().split())

alist=[0]*3
blist=[0]*3

xlist=[4,2,1]
for i in range(3):
    x=xlist[i]
    if a>=x:
        alist[i]=1
        a-=x
    if b>=x:
        blist[i]=1
        b-=x

ans=0
for i in range(3):
    if alist[i]==1 or blist[i]==1:
        ans+=xlist[i]

print(ans)
