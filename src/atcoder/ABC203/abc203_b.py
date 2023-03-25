nk=list(map(int,input().split()))
n=nk[0]
k=nk[1]

ans=0
for i in range(1,n+1):
    for j in range(1,k+1):
        ans+=i*100+j
print(ans)