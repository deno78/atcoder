# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))
wf={}
for i in range(n):
    wf[i]=[]
for i in range(m):
    u,v,b=map(int,input().split())
    u-=1
    v-=1
    wf[u].append([v,b])
    wf[v].append([u,b])

# solve
wk=[]
wk.append([0,alist[0]])

ans=[float("INF")]*n

while len(wk)>0:
    w=wk.pop(0)
    u=w[0]
    c=w[1]
    for v,b in wf[u]:
        x=c+b+alist[v]
        if int(ans[v])>x:
            ans[v]=str(x)
            wk.append([v,x])
# answer
print(" ".join(ans))
