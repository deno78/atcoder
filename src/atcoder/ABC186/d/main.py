n=int(input())
alist=list(map(int,input().split()))
alist.sort()
sum=0
sum1=0
for i in range(0,n):
#    print("[1]alist[{}]*{}".format(i,i))
    sum1+=(i)*alist[i]

sum2=0
for i in range(0,n-1):
#    print("[2]alist[{}]*{}".format(i,n-i-1))
    sum2+=alist[i]*(n-i-1)

print(sum1-sum2)