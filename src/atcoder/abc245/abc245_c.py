# TODO edit the code

# param
n,k = map(int,input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

if n==1:
    print('Yes')
    exit()
    
# solve
dlist=[]
for i in range(n-1):
    a1=alist[i]
    a2=alist[i+1]
    b1=blist[i]
    b2=blist[i+1]
    dlist.append(min(abs(a1-a2),abs(a1-b2),abs(b1-a2),abs(b1-b2)))

if max(dlist)>k:
    print('No')
else:
    print('Yes')
