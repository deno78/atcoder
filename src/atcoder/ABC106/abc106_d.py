nmq = list(map(int,input().split()))
n=nmq[0]
m=nmq[1]
q=nmq[2]

lrlist=[]
for i in range(m):
    lrlist.append(list(map(int,input().split())))

pqlist=[]
for i in range(q):
    pqlist.append(list(map(int,input().split())))

ans=[]
for i in range(n+1):
    ans.append([])
    for j in range(n+1):
        ans[i].append(0)
clm=[]
for i in range(n+1):
    clm.append([])
    for j in range(n+1):
        clm[i].append(0)

for j in range(1,n+1):
    for i in range(1,n+1):
        c=0
        for lr in lrlist:
            l = int(lr[0])
            r = int(lr[1])
            if l == i and r == j:
                c=c+1
        ans[i][j]=c

for j in range(1,n+1):
    for i in range(1,n+1):
        c=0
        # 上と左のマスから加えたあと、二重に足されてしまうので左上マスを引く
        clm[i][j]=clm[i-1][j] + clm[i][j-1] -clm[i-1][j-1] +ans[i][j]
for an in clm:
    print(an)

for pq in pqlist:
    c=0
    print(pq)
    p=pq[0]
    q=pq[1]
    print("{}/{}/{}/{}".format(clm[q][q],clm[p][q],clm[q][p],clm[p][p]))
    print(clm[q][q]-clm[p][q]-clm[q][p]+clm[p][p])

