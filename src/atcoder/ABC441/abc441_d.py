from collections import deque

n,m,l,s,t=map(int,input().split())
uvc=[]

for i in range(m):
    u,v,c=map(int,input().split())
    u-=1
    v-=1
    uvc.append([u,v,c])

uvdict={}
for i in range(n):
    uvdict[i]=[]

for u,v,c in uvc:
    uvdict[u].append([v,c])

ans=set()
wk=deque()
wk.append([0,0,0])
while len(wk)>0:
    w=wk.popleft()
    current=w[0]
    total=w[1]
    step=w[2]
    for x in uvdict[current]:
        next=x[0]
        cost=x[1]
        if s<=(total+cost) and (total+cost)<=t and l==step+1:
#            print(current,"->",next,total,cost,step+1)
            ans.add(next+1)
        if total+cost<=t and step+1<=l:
            wk.append([next,total+cost,step+1])

print(" ".join(map(str, sorted(ans))))