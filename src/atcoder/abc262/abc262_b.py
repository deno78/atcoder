n,m=map(int,input().split())
uv={}
for i in range(m):
    u,v=map(int,input().split())
    if u not in uv.keys():
        uv[u]=[]
    uv[u].append(v)
    if v not in uv.keys():
        uv[v]=[]
    uv[v].append(u)

ans=0
for i in uv.keys():
    for j in uv[i]:
        if j in uv.keys():
            for k in uv[j]:
                if i in uv[k] and i < j and j < k:
                    ans+=1

print(ans)


