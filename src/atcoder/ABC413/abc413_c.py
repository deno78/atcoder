from collections import deque
q=int(input())
query=[]
for i in range(q):
    query.append(list(map(int, input().split())))

alist=deque([])
for i in range(q):
    q=query[i]
    if q[0]==1:
        c=q[1]
        x=q[2]
        alist.append([x,c])
    elif q[0]==2:
        k=q[1]
        y=0
        while k>0:
            h=alist.popleft()
            x=h[0]
            c=h[1]
            if c>k:
                y+=x*k
                c2=c-k
                alist.appendleft( [x, c2])
                k=0
            else:
                y+=x*c
                k-=c
        print(y)
