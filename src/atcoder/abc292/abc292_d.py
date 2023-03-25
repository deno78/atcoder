# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
uv={}
for i in range(n):
    uv[i]={}
for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    if v not in uv[u].keys():
        uv[u][v]=0
    uv[u][v]+=1
    if u not in uv[v].keys():
        uv[v][u]=0
    uv[v][u]+=1

# solve
checked=[0]*n
ans=[]
for i in range(n):
    if checked[i]==0:
        wk=[i]
        lines=0
        points=1
        checked[i]=1
        while len(wk)>0:
            w=wk.pop(0)
            for v,s in uv[w].items():
                lines+=s
#                print("[{}] -> {} [{}] =>{}".format(w,v,s ,lines))
                if checked[v]==0:
                    points+=1
                    wk.append(v)
                    checked[v]=1
        lines//=2
        if lines!=points:
            print("No")
            exit()

# answer
print("Yes")
