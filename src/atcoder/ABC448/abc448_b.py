n,m=map(int,input().split())
clist=list(map(int,input().split()))
ab=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append((a,b))

ans=0
for i in range(n):
    a,b=ab[i]
    x=min(b,clist[a-1])
    ans+=x
    clist[a-1]-=x

print(ans)