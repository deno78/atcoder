n,p=map(int,input().split())
alist=list(map(int,input().split()))

ans=0
for a in alist:
    if a <p:
        ans+=1
print(ans)