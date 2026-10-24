n,k=map(int,input().split())
alist=list(map(int,input().split()))

ans=0
for i in range(1,n):
    if (alist[i-1]<k and k<alist[i]) or (alist[i-1]>k and k>alist[i]) or alist[i-1]==k:
#        print(i-1,i,alist[i-1],alist[i])
        ans+=1
if alist[-1]==k:
    ans+=1

print(ans)