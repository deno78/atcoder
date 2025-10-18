from collections import deque


q=int(input())
queries=[]
for i in range(q):
    queries.append(input().split())

s=deque()
x1=0
x2=0
b=deque()
b2=deque()

for query in queries:
    if query[0]=="1":
        c=query[1]
        s.append(c)
        if c=="(":
            x1+=1
        elif c==")":
            x2+=1
        b.append(x1-x2)
        if len(b2)==0:
            b2.append(x1-x2)
        elif b2[-1]>(x1-x2):
            b2.append(x1-x2)
        else:
            b2.append(b2[-1])
    elif query[0]=="2":
        c=s.pop()
        if c=="(":
            x1-=1
        elif c==")":
            x2-=1
        b.pop()
        b2.pop()
    if len(s)==0 or (b2[-1]>=0 and x1==x2):
        print("Yes")
    else:
        print("No")