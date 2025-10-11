from collections import deque

n,m=map(int,input().split())
uv={}
for i in range(n):
    uv[i]=set()
ans_1=0
for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    if u==v:
        ans_1+=1
    else:
        if v not in uv[u]:
            uv[u].add(v)
        else:
            ans_1+=1
        if u not in uv[v]:
            uv[v].add(u)
        else:
            ans_1+=1

ans=99999999999999
for i in range(n):
    wk=deque()
    wk.append([i,0,[0]*n])
    wk[0][2][i]=1
    while len(wk)>0:
        a,c,colors=wk.pop()
        for v in uv[a]:
            if colors[v]>0 and colors[v]%2==colors[a]%2:
                c+=1
        for v in uv[a]:
            if colors[v]==0:
                wk.append([v,c,colors])
                wk[-1][2][v]=colors[a]+1
        if min(colors)>0:
            ans=min(ans,c)

print(ans+ans_1//2)