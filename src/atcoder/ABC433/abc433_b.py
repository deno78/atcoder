n=int(input())
alist=list(map(int,input().split()))

for i in range(n):
    ans=-1
    for j in range(1,i+1):
#        print(i,j,alist[i],alist[i-j])
        if i-j>=0 and alist[i]<alist[i-j]:
            ans=i-j+1
            break
    print(ans)

