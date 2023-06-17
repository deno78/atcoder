n,m=map(int,input().split())
r={}
for i in range(n):
    r[i]=[]
for i in range(m):
    a,b=map(int,input().split())
    r[a-1].append(b-1)
    r[b-1].append(a-1)
for i in range(n):
    print(len(r[i]))
