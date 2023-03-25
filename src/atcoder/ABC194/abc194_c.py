n=int(input())
alist=list(map(int,input().split()))

s=sum(alist)
ans=0
for i in range(n):
    a=alist[i]  
    ans+=2*(a**2)*(n-1)
    ans-=2*a*(s-a)

print(int(ans/2))
