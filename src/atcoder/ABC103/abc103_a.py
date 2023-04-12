a=list(map(int,input().split()))

ans=float("INF")

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=j and j!=k and i!=k:
                wk=0
                wk+=abs(a[i]-a[j])
                wk+=abs(a[j]-a[k])
                ans=min(ans,wk)
#                print("[{},{},{}]={}-{} {}-{} =>{}".format(i,j,k,a[i],a[j],a[j],a[k],wk))

print(ans)