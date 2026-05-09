n,k=map(int,input().split())
alist=[]
for i in range(n):
    alist.append(list(map(int,input().split())))

clist=list(map(int,input().split()))

for i in range(n):
    a=alist[i]
    c=clist[i]
    l=a[0]
    l2=l*c
    if l2>=k:
        k2=k%l-1
#        print(alist[i][1:],k2)
        print(alist[i][1:][k2])
        exit()
    else:
        k-=l2