# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
q = int(input())
xy=[]
for i in range(q):
    xy.append(list(map(int,input().split())))

# solve
ab=[]
for i in range(n+1):
    ab.append([0]*(n+1))

if alist[0]==blist[0]:
    ab[0][0]=1

for i in range(n):
    for j in range(n):
        if alist[i]==blist[j]:
            ab[i][j+1]=ab[i][j]+1
            ab[i+1][j]=ab[i][j]+1
        else:
            ab[i][j+1]=ab[i][j]
            ab[i+1][j]=ab[i][j]

for a in ab:
    print(a)

for x,y in xy:
    print(ab[x-1][y-1])