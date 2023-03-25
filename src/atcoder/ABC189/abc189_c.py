n = int(input(''))
alist = list(map(int,input('').split()))
 
ans=0
for l in range(n):
    A = alist[l]
    for r in range(l,n):
        B = alist[r]
        x = min(A,B)
        x2 = x*(r-l+1)
        print("{}-{}-{} ({})".format(l,r,x,ans))
        ans= max(ans,x2)
 
print(ans)