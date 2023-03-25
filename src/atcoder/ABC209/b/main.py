n,x=map(int,input().split())

alist=list(map(int,input().split()))

y=0
for i in range(len(alist)):    
    a=alist[i]
    if i%2==1:
        a=alist[i]-1
    y+=a
if x>=y:
    print('Yes')
else:
    print('No')