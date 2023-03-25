n=int(input())
plist=list(map(int,input().split()))

ans=0
for i in range(1,n-1):
    p=plist[i-1:i+2]
#    print(p)
    p1=p[1]
    p.sort()
    p2=p[1]
    if p1==p2:
        ans+=1
print(ans)
