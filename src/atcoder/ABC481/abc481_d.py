from collections import deque

n,m,s,t=map(int,input().split())
routes={}
for i in range(n):
    routes[i]=[]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    routes[a].append(b)

s-=1
t-=1
min_routes={}
for i in routes.keys():
    if len(routes[i])==0:
        min_routes[i]=float("INF")
    else:
        min_routes[i]=min(routes[i])

wk=deque()
wk.append(s)
costs=[float("INF")]*n
costs[s]=0

while len(wk)>0:
    current=wk.popleft()
    cost=costs[current]
    for next_node in routes[current]:
        if next_node==min_routes[current]:
            next_cost=cost
            if next_node==t:
                costs[next_node]=min(costs[next_node],next_cost)
            else:
                if costs[next_node]>next_cost:
                    costs[next_node]=next_cost
                    wk.appendleft(next_node)
        else:
            next_cost=cost+1
            if next_node==t:
                costs[next_node]=min(costs[next_node],next_cost)
            else:
                if costs[next_node]>next_cost:
                    costs[next_node]=next_cost
                    wk.append(next_node)


if costs[t]==float("INF"):
    print(-1)
else:
    print(costs[t])