n,m=map(int,input().split())
alist=list(map(int,input().split()))

wk=0
for i in range(1,m+1):
    wk+=i*alist[i]
ans=wk
for i in range(n-m):
    print("{} - {} + {}".format(wk,alist[i],alist[i+m]))
    wk-=alist[i]
    wk+=alist[i+m]
    ans=max(ans,wk)

print(ans)