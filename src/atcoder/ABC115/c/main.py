n,k=map(int,input().split())
hlist=[]
for i in range(n):
    hlist.append(int(input()))

hlist.sort()
ans=float('INF')
for i in range(n-k+1):
    h1=hlist[i]
    h2=hlist[i+k-1]
    # print("[{}] {}-{}".format(i,h1,h2))
    ans=min(ans,h2-h1)

print(ans)
