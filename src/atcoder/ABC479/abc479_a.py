n=int(input())
alist=list(map(int,input().split()))
ans=0
for i in range(n):
    if i%2==0:
        ans+=alist[i]
print(ans)