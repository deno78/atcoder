# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import itertools

# param
n = int(input())
Mg = int(input())
uv=[]
for i in range(Mg):
    u,v=map(int,input().split())
    u-=1
    v-=1
    uv.append("{}#{}".format(u,v))
uv.sort()
Mh = int(input())
ab=[]
for i in range(Mh):
    a,b=map(int,input().split())
    a-=1
    b-=1
    ab.append("{}#{}".format(a,b))
ab.sort()

amap=[]
for i in range(n):
    amap.append([-1]*n)
for i in range(n-1):
    a=list(map(int,input().split()))
    for j in range(len(a)):
        amap[i][i+j+1]=a[j]
        amap[j+i+1][i]=a[j]

# solve
ans=float("INF")
slist=list(itertools.permutations(range(n)))
for r2 in slist:
    tmp=0
    ab2=[]
    t={}
    for i in range(n):
        t[str(i)]=str(r2[i])
    for x in ab:
        ab2.append(x.translate(str.maketrans(t)))
    w=[]
    for i in range(n):
        w.append([0]*n)
    for x in uv:
        if x not in ab2:
            a,b=map(int,x.split("#"))
            w[a][b]=amap[a][b]
            w[b][a]=amap[a][b]
    for x in ab2:
        if x not in uv:
            a,b=map(int,x.split("#"))
            w[a][b]=amap[a][b]
            w[b][a]=amap[a][b]
    tmp=0
    for x in w:
        tmp+=sum(x)
    tmp=tmp//2
    ans=min(ans,tmp)    


# answer
print(ans)