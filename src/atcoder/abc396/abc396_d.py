# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
n,m = map(int, input().split())
uv={}
for i in range(n):
    uv[i]=[]
wmap=[]
for i in range(n):
    wmap.append([-1]*n)
for i in range(m):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    uv[u].append(v)
    uv[v].append(u)
    wmap[u][v]=w
    wmap[v][u]=w

wk=deque()
wk.append([0,[0]])

ans=float("INF")
while len(wk)>0:
    x=wk.popleft()
    w1=x[0]
    x1=x[1][-1]
    for x2 in uv[x1]:
        if x2 not in x[1]:
            w2=w1^wmap[x1][x2]
            xn=[w2,x[1]+[x2]]
#            print(xn)
            if x2==n-1:
                ans=min(ans,xn[0])
            else:
                wk.append(xn)

# answer
print(ans)