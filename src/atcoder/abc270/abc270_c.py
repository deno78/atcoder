n,x,y=map(int,input().split())

path={}
f=[-1]*(n+1)
for i in range(n-1):
    u,v=map(int,input().split())
    if u not in path.keys():
        path[u]=[]
    if v not in path.keys():
        path[v]=[]
    path[u].append(v)
    path[v].append(u)

cur=[]
cur.append([x,str(x)])
f[x]=0
while len(cur)>0:
    c,arr = cur.pop()
    for next in path[c]:
        if f[next]==-1:
            arr_next=arr+ " " + str(next)
            f[next]=1
            cur.append([next,arr_next])
            if next==y:
                print(arr_next)
                exit()
    path[c].clear()
