# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
n,q = map(int, input().split())
qlist=[]
for i in range(q):
    q=input().split()
    qlist.append(q)

# solve
d=[]
for i in range(n):
    d.append([n-i,0])

for q in qlist:
    a=q[0]
    b=q[1]
    if a=='1':
        hx=d[-1][0]
        hy=d[-1][1]
        if b=='R':
            hx+=1
        elif b=='L':
            hx-=1
        elif b=='U':
            hy+=1
        elif b=='D':
            hy-=1
        d.append([hx,hy])
    elif a=='2':
        xy=d[-1*int(b)]
        # answer
        print("{} {}".format(xy[0],xy[1]))