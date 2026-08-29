n=int(input())
alist=list(map(int,input().split()))
ans=0
for i in range(n//2):
    ans+=alist[i+n//2]
print(ans)