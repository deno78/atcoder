# TODO edit the code

# param
n,q = map(int,input().split())
xlist=[]
for i in range(q):
    xlist.append(input())
alist=[]
adic={}
for i in range(n):
    adic[str(i+1)]=i
    alist.append(str(i+1))

# solve
for a1 in xlist:
    i1=adic[a1]
    i2=i1+1
    if i1+1==n:
        i2=i1-1
    a2=alist[i2]

    adic[a2]=i1
    adic[a1]=i2
    alist[i1]=a2
    alist[i2]=a1
#    print(alist)

# answer
print(" ".join(alist))