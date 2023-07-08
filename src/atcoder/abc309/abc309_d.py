# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
n1,n2,m= map(int, input().split())
ab={}
for i in range(n1+n2):
    ab[i]=[]

for i in range(m):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    ab[a].append(b)
    ab[b].append(a)

# solve
bfs=[-1]*(n1+n2)
wk=deque()
wk.append(0)
wk.append(n1+n2-1)
bfs[0]=0
bfs[n1+n2-1]=0
while len(wk)!=0:
    w=wk.popleft()
    for x in ab[w]:
        if bfs[x]==-1:
            bfs[x]=bfs[w]+1
            wk.append(x)
    ab.pop(w)
#    print(bfs)

#print(bfs[:n1])
#print(bfs[n1:])
# answer

print(max(bfs[:n1])+max(bfs[n1:])+1)