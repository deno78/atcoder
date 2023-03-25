# TODO edit the code

# param
n,k=map(int,input().split())
alist=list(map(int,input().split()))

alist2=[]
for i in range(k):
    alist2.append([])

for i in range(n):
    alist2[i%k].append(alist[i])

for a2 in alist2:
    a2.sort()

# solve
for i in range(n-1):
    x1=i//k
    y1=i%k
    x2=(i+1)//k
    y2=(i+1)%k
    a1=alist2[y1][x1]
    a2=alist2[y2][x2]
    if a1>a2:
        print('No')
        exit()
print('Yes')