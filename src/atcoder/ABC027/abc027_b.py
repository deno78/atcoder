n=int(input())
alist=list(map(int,input().split()))

v=sum(alist)//n
if sum(alist)/n != sum(alist)//n:
    print(-1)
    exit()

ans=0
l=0
r=1
w=alist[0]
while l<n and r<n+1:
    if w//(r-l)==v:
#        print("{}-{}:N:{}".format(l,r,alist[l:r]))
        l=r
        r=l+1
        w=0
    else:
#        print("{}-{}:E:{}".format(l,r,alist[l:r]))
        w+=alist[r]
        r+=1
        ans+=1

print(ans)