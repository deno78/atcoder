n,m=map(int,input().split())

INF=float('INF')

route=[]
for i in range(n):
    route.append([INF]*n)

for i in range(m):
    a,b,c=map(int,input().split())
    route[a-1][b-1]=c

cnt=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j:
                m2=min(k+1,n)
                for m in range(k,m2):
                    if route[i][m]!=INF and route[m][j]!=INF:
                        route[i][j]=min(route[i][j],route[i][m]+route[m][j])

    for i in range(n):
        #print(route[i])
        for j in range(n):
            x=route[i][j]
            if i!=j and x!= INF:
                cnt+=x
print(cnt)