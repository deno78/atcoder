# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
uv={}
for i in range(n):
    uv[i]=[]
for i in range(n-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    uv[u].append(v)
    uv[v].append(u)

# solve
ans=[]
chk=[0]*n
chk[0]=1
for x in uv[0]:
    a=0
    wk=[]
    wk.append(x)
    while len(wk)>0:
        w=wk.pop(0)
        for v in uv[w]:
            if chk[v]==0:
                a+=1
                chk[v]=1
                wk.append(v)
    ans.append(a)

# answer
print(n-max(ans))