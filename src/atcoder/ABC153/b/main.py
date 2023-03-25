h,n=map(int,input().split())

alist=list(map(int,input().split()))

for a in alist:
    h-=a
if h>0:
    print('No')
else:
    print('Yes')
    