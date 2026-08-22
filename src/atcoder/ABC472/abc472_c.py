n,m,k=map(int,input().split())
alist=list(map(int,input().split()))

wk=0
eaten=[0]*n
for i in range(n):
    a=alist[i]
    a2=0
    if i>=m and eaten[i-m]==1:
        a2=alist[i-m]
    if wk+a-a2<=k:
        print("Yes")
        eaten[i]=1
        wk+=a
    else:
        print("No")
    wk-=a2
#    print(i,max(-1,i-m),a,a2,wk)
