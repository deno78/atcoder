n=int(input())
tlist=list(map(int,input().split()))

m=int(input())
px=[]
for i in range(m):
    p,x=map(int,input().split())
    p-=1
    px.append([p,x])

ans=sum(tlist)
for i in range(m):
    p,x=px[i]
    print(ans-tlist[p]+x)
