n,t=map(int,input().split())
alist=[]
for i in range(n):
    alist.append(int(input()))

ans=t*n
for i in range(1,n):
    ans-=max(0,alist[i-1]+t-alist[i])

print(ans)