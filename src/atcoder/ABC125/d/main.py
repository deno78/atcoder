n=int(input())
alist=list(map(int,input().split()))
sum1=sum(alist)
ans=0
m=n-1
blist=[]
for i in range(n-1):
    s2=0
    s2-=alist[i]
    s2-=alist[i+1]
    s2+=-1*alist[i]
    s2+=-1*alist[i+1]
    blist.append(i)
print(blist)

for i in range(2**m):
    sum2=0
    bag=[]
    for j in range(m):
        if (i>>j) &1:
            sum2+=blist[j]
            bag.append(j)
    print("{}:{}".format(sum2,bag))
    ans=max(sum2,ans)

print(sum1+ans)