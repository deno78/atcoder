n,k=map(int,input().split())
hlist=list(map(int,input().split()))

c=0
for h in hlist:
    if h>=k:
        c+=1

print(c)