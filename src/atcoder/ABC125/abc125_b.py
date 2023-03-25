n=int(input())
vlist=list(map(int,input().split()))
clist=list(map(int,input().split()))

ans=0
for i in range(n):
    x=vlist[i]-clist[i]
    if x>0:
        ans+=x

print(ans)
