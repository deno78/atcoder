def check(m,t,w):
    for a,b in r[m]:
        if a==t:
            return max(b,w)
        else:
            w=max(w,check(a,t,w))

n=int(input())

r={}

for i in range(n-1):
    u,v,w = map(int,input().split())
    u-=1
    v-=1
    if u not in r.keys():
        r[u]=[]
    if v not in r.keys():
        r[v]=[]
    r[u].append([v,w])
    r[v].append([u,w])

print(r)
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        print("{}->{}".format(i,j))
        ans+=check(i,j,0)

print(ans)

