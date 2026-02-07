n,k=map(int,input().split())

ans=0
for i in range(1,n+1):
    s=str(i)
    w=0
    for j in range(len(s)):
        w+=int(s[j])
    if w==k:
        ans+=1

print(ans)

