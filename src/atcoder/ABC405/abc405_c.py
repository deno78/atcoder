n=int(input())
alist=list(map(int,input().split()))
x=sum(alist)

ans=0
for i in range(n-1):
    a=alist[i]
    x-=a
    ans+=x*a

print(ans)
