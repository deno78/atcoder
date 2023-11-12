# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import itertools

# param
n,m,k = map(int, input().split())

d=[]
d2=[]
for i in range(n):
    d.append([float("INF")]*n)
    d2.append([0]*n)
for i in range(m):
    u,v,w= map(int, input().split())
    u-=1
    v-=1
    d[u][v]=w
    d[v][u]=w

# solve
ans=[]
for x in d:
    print(x)

# answer
print("{}".format(sum(ans)%k))
