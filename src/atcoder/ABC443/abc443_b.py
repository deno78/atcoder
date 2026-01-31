n,k=map(int,input().split())

ans=0
wk=0
while True:
    wk+=n
    if wk>=k:
        break
    n+=1
    ans+=1

print(ans)