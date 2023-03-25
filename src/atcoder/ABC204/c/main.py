nm=input().split()
n=int(nm[0])
m=int(nm[1])

d=[]
for i in range(n):
    d.append([float('INF')]*(n))

for i in range(n):
    d[i][i]=0

for i in range(m):
    ab=input().split()
    a=int(ab[0])-1
    b=int(ab[1])-1
    d[a][b]=1

for i in range(n):
    for j in range(n):
        for k in range(n):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j],d[j][i])

e=0
for i in range(n):
    for j in range(n):
#        print("{}:{} =>{}".format(i,j,d[i][j]))
        if d[i][j]!=float('INF'):
            e+=1
print(e)