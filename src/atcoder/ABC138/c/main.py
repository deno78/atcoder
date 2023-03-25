n=int(input())
alist=list(map(int,input().split()))

alist.sort()

t=alist[0]
for i in range(1,n):
    t=(t+alist[i])/2

print(t)