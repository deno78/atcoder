from collections import deque

n,m=map(int,input().split())
yxdict={}
for i in range(n):
    yxdict[i]=[]
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    yxdict[y].append(x)
q=int(input())
blist=[0]*n
#print(xydict)
for _ in range(q):
    q=list(map(int,input().split()))
    q1=q[0]
    q2=q[1]
    q2-=1
    if q1==1:
        if blist[q2]==0:
            wk=deque([q2])
            while len(wk)>0:
                w=wk.popleft()
                blist[w]=1
                for nx in yxdict[w]:
                    if blist[nx]==0:
                        wk.append(nx)
    elif q1==2:
        if blist[q2]==1:
            print("Yes")
        else:
            print("No")




