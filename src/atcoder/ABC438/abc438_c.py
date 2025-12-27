def check(l,r):
    print(l,r,alist[l],alist[r])
    if alist[l]==-1 or alist[r]==-1:
        return
    if alist[l]!=alist[r]:
        return
    while l>0 and alist[l-1]==alist[r]:
        l-=1
    while r<n-1 and alist[l]==alist[r+1]:
        r+=1
    if r-l>=4:
        print("->",l,r,alist[l],alist[r])

        for i in range(l,r-1):
            alist[i]=-1
        if l>0 and r<n:
            check(l-1,r)
    

n=int(input())
alist=list(map(int,input().split()))

for i in range(n-1):
    check(i,i+1)

print(alist)