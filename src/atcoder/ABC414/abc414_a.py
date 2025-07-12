n,l,r=map(int,input().split())
xy=[]
for i in range(n):
    x,y=map(int,input().split())
    xy.append((x,y))
ans=0
for x,y in xy:
    if x<=l and r<=y:
        ans+=1

print(ans)
