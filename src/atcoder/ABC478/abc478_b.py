n,v=map(int,input().split())
wlist=list(map(int,input().split()))

ans=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            # print(i,j,k,v-2,wlist[i]+wlist[j]+wlist[k])
            if i+j+k<v-2:
                ans=max(ans,wlist[i]+wlist[j]+wlist[k])

print(ans)