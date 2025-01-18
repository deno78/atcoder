# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
q = int(input())
qlist=[]
for i in range(q):
    qlist.append(input().split())

# solve
wk2=deque([])
t=0
d=0
for query in qlist:
    i=query[0]
    if i=="1":
        l=int(query[1])
        t+=l
        wk2.append(t)
    elif i=="2":
        w=wk2.popleft()
        w-=d
        d+=w
    elif i=="3":
        k=int(query[1])
        if k==1:
            print(0)
        else:
            print(wk2[k-2]-d)
#    print("[{}] {} / {}".format(query,d,wk2))
