# TODO edit the code

# param
n,m,k,s,t,x = map(int,input().split())
uv ={}
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

#print(uv)
MOD=998244353
ans=0
r1=[0]*n
r2=[0]*n

r1[s]=1
r2[s]=0
p=[]
p.append(s)
for i in range(k):    
    p2=set([])
    for c in p:
        if c==x:
            r=r2[c]
            for v in uv[c]:
                r1[v]=r1[v]+r
                p2.add(v)
        else:
            r=r1[c]
            for v in uv[c]:
                r2[v]=r2[v]+r
                p2.add(v)
    p=list(p2)
print(r1)
# answer
print(ans)
