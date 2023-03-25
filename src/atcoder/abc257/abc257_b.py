# TODO edit the code

# param
n,k,q=map(int,input().split())
alist=list(map(int,input().split()))
llist=list(map(int,input().split()))

for i in range(q):
    l=llist[i]-1
    a=alist[l]
    if a!=n:
        a2=a+1
        if a2 not in alist:
            alist[l]=a2

print(" ".join(map(str,alist)))    
