n,m=map(int,input().split())
ab={}
for i in range(n):
    a,b=map(int,input().split())
    if a not in ab.keys():
        ab[a]=0
    ab[a]+=b

ans=0
for a,b in sorted(ab.items()):
    x=min(m,b)
    ans+=(x*a)
    m-=x
    if m<=0:
        break


print(ans)