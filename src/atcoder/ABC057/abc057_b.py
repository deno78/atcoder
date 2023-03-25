n,m=map(int,input().split())

ab=[]
cd=[]
for i in range(n):
    a,b=map(int,input().split())
    ab.append([a,b])
for i in range(m):
    c,d=map(int,input().split())
    cd.append([c,d])


for i in range(n):
    ans=-1
    min_d=float('INF')
    a,b=ab[i]
    for j in range(m):
        c,d=cd[j]
        d=abs(a-c) + abs(b-d)
#        print("[{}/{}] {}/{}".format(i,j,ans,min_d))
        if min_d > d:
            ans=j+1
            min_d=d
    print(ans)