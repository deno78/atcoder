# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
n,m = map(int, input().split())
wmap=[]
uv={}
for i in range(n):
    wmap.append([0]*n)
    uv[i]=[]

for i in range(m):
    u,v,w=map(int, input().split())
    u-=1
    v-=1
    wmap[u][v]=w
    wmap[v][u]=-1*w
    uv[u].append(v)
    uv[v].append(u)
flg=[0]*n
ans=[0]*n

# solve
for i in range(n):
    if flg[i]==0:
        wk=deque([i])
        while len(wk)>0:
            x1=wk.popleft()
            flg[x1]=1
            a=ans[x1]
            for x2 in uv[x1]:
                if flg[x2]==0:
                    flg[x2]=1
                    ans[x2]=a+wmap[x1][x2]
                    wk.append(x2)
#                    print("[{}]={}".format(x2,ans[x2]))
            uv[x1]=[]

# answer
ans2 = [str(i) for i in ans]

print(" ".join(ans2))
