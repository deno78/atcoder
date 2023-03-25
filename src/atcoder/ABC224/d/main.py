m=int(input())

uv=[]
for i in range(m):
    uv.append(list(map(int,input().split())))

plist=list(map(int,input().split()))

INF=float('INF')
root=[]
for i in range(9):
    root[i][i]=0

for i in range(9):
    root.append([INF]*9)

for u,v in uv:
    root[u-1][v-1]=1
    root[v-1][u-1]=1

for k in range(9):
    for i in range(9):
        for j in range(9):
            if root[i][k]!=INF and root[k][j]!=INF:
                root[i][j] = min(root[i][j], root[i][k]+root[k][j])

for r in root:
    print(r)

ans=0
for i in range(8):
    p=plist[i]-1 
    if p != i:
        print("{}->{} = {}".format(p,i,root[p][i]))
        ans+=root[p][i]

print(ans)
