n=int(input())
plist=list(map(int,input().split()))

ans=1
m=plist[0]
for i in range(1,n):
    p=plist[i]
    if p<m:
        ans+=1
        m=p
print(ans)
