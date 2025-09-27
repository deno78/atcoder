n=int(input())
ans=0
for i in range(1,n+1):
    w=i**3*(-1)**i
    ans+=w
print(ans)