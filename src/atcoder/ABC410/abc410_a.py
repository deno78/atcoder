n=int(input())
alist=list(map(int,input().split()))
k=int(input())

ans=0
for a in alist:
    if k<=a:
        ans+=1
print(ans)