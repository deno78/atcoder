# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())

abxy={}
for i in range(m):
    a,b,x,y=map(int,input().split())
    if a not in abxy.keys():
        abxy[a]={}
    if b not in abxy.keys():
        abxy[b]={}
    abxy[a][b]=[x,y]
    abxy[b][a]=[-1*x,-1*y]
# solve
ans={}
for i in range(n+1):
    ans[i]=[]
ans[1]=[0,0]
wk=[]
wk.append(1)
while len(wk)>0:
    w=wk.pop(0)
    x1=ans[w][0]
    y1=ans[w][1]
    for b in abxy[w]:
        if len(ans[b])==0:
#            print(abxy[w][b])
            x2=x1+abxy[w][b][0]
            y2=y1+abxy[w][b][1]
            ans[b]=[x2,y2]
            wk.append(b)
        elif len(ans[b])>2:
            x2=x1+abxy[w][b][0]
            y2=y1+abxy[w][b][1]
            x3=ans[b][0]
            y3=ans[b][1]
            if x3!=x2 or y3!=y2:
                ans[b].append(x2)
                ans[b].append(y2)

# answer
for i in range(n):
    if len(ans[i+1])==2:
        print("{} {}".format(ans[i+1][0],ans[i+1][1]))
    else:
        print("undecidable")
