# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
n,w = map(int, input().split())
bmap=[-1]*w
wk=deque()
for i in range(n):
    x,y=map(int,input().split())
    x-=1
    y-=1
    if y==0:
        bmap[x]=i
    wk.append([x,y,i])
q=int(input())
qlist=[]
for i in range(q):
    t,a=map(int,input().split())
    a-=1
    qlist.append([t,a])
ans=[-1]*n
bmap_count=0
t=0
T_MAX=10**100
while len(wk)>0 and t<=T_MAX:
    sz=len(wk)
    for i in range(sz):
        x,y,a=wk.popleft()
        if y==1 and bmap[x]==-1:
            bmap[x]=a
            bmap_count+=1
            chk=True
        elif y==1 and bmap[x]!=-1:
            wk.append([x,y,a])
        elif y>1:
            wk.append([x,y-1,a])
    print(wk)
    print(bmap_count)
    if bmap_count==w:
        for i in range(w):
            ans[bmap[i]]=t
        bmap=[-1]*w
        bmap_count=0
    t+=1

for t,a in qlist:
#    print("{} {}".format(ans[a],t))
    if ans[a]>=t or ans[a]==-1:
        print("Yes")
    else:
        print("No")
