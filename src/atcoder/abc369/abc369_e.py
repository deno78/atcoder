# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
uvt=[]
uv1={}
for i in range(n):
    uv1[i]=[]
for i in range(m):
    u,v,t=map(int, input().split())
    u-=1
    v-=1
    uvt.append([u,v,t])
    uv1[u].append(v)
    uv1[v].append(u)

q=int(input())
qlist=[]
for i in range(q):
    k=int(input())
    blist=list(map(int,input().split()))
    qlist.append(blist)

uv2=[]
for i in range(n):
    uv2.append([float("INF")]*n)
for i in range(m):
    u,v,t=uvt[i]
    uv2[u][v]=min(uv2[u][v],t)
    uv2[v][u]=min(uv2[v][u],t)

# solve
wk=[]
wk.append([0,0])
while len(wk)>0:
    w=wk.pop(0)
    u=w[0]
    d=w[1]
    for v in uv1[u]:
        t=uv2[u][v]
        uv2[u][v]=

# answer
print("{} {}".format(ans, s))
