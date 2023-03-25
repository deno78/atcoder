n,k=map(int,input().split())

alist=list(map(int,input().split()))

xy1=[]
xy2=[]
for i in range(1,n+1):
    if i in alist:
        xy2.append(list(map(int,input().split())))
    else:
        xy1.append(list(map(int,input().split())))

ans=-1

for x1,y1 in xy1:
    d=float('INF')
    for x2,y2 in xy2:
        d=min(d,(x1-x2)**2 + (y1-y2)**2)
    ans=max(ans,d)

print(ans**0.5)
