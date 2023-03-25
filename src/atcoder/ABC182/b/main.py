n=int(input())
alist=list(map(int,input().split()))

ans=1
c1=-1
for i in range(2,1000):
    c2=0
    for a in alist:
        if a%i==0:
#            print("{}/{}".format(a,i))
            c2+=1
    if c2>c1:
        c1=c2
        ans=i

print(ans)