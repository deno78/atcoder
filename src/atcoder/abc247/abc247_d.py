from collections import deque

# TODO edit the code

# param
n = int(input())
query=[]
for i in range(n):
    query.append(list(map(int,input().split())))

que=deque()

# solve
for q in query:
#    print(que)
    if q[0]==1:
        que.append([q[1],q[2]])
    elif q[0]==2:
        s=0
        c=q[1]
        while c>0:
            t=que.popleft()
            x=t[0]
            c2=t[1]
            if c>c2:
                s+=x*c2
                c-=c2
            else:
                s+=x*(min(c,c2))
                if c2-c>0:
                    que.appendleft([x,c2-c])
                c-=c2
        print(s)

