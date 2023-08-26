# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
n,m= map(int, input().split())
ab={}
ac={}
for i in range(1,n+1):
    ab[i]=[]
    ac[i]={}
for i in range(m):
    a,b,c = map(int,input().split())
    ab[a].append(b)
    ab[b].append(a)
    ac[a][b]=c
    ac[b][a]=c

# solve
ans=-1
for i in range(1,n+1):
    wk=deque()
    wk.append([i,0,[0]*(n+1)])
    while len(wk)>0:
        w=wk.popleft()
        l=w[0]
        c=w[1]
        ans=max(ans,c)
        u=w[2]
        for b in ab[l]:
            if u[b] ==0:
                u[b]=1
                wk.append([b,c+ac[l][b],u])


# answer
print("{}".format(ans))
