n,m=map(int,input().split())
uv={}
for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    if u not in uv.keys():
        uv[u]=[]
    if v not in uv.keys():
        uv[v]=[]
    uv[u].append(v)
    uv[v].append(u)

visited=[0]*n

groups=[]
for i in range(n):
    if visited[i]==0:
        wk=[i]
        group=[i]
        while len(wk)>0:
            x = wk.pop()
            for j in uv[x]:
                if visited[j]==0:
                    wk.append(j)
                    group.append(j)                
                    visited[j]=1
        groups.append(group)

print(len(groups))