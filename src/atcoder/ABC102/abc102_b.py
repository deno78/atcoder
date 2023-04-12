n=int(input())
alist=list(map(int,input().split()))

ans=-1
for i in range(n-1):
    for j in range(i,n):
        ans=max(ans,abs(alist[i]-alist[j]))

print(ans)