# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,d = map(int, input().split())
xy=[]
for i in range(n):
    x,y=map(int,input().split())
    xy.append([x,y])

# solve
nmap=[]
for i in range(n):
    nmap.append([-1]*n)

for i in range(n-1):
    for j in range(i+1,n):
        x1,y1=xy[i]
        x2,y2=xy[j]
        z=(x1-x2)**2+(y1-y2)**2
        nmap[i][j]=z
        nmap[j][i]=z
ans=[]
for i in range(1,n):
    ans.append(i)
wk=[0]
d1=d**2
while len(wk)>0:
    w=wk.pop()
    for a in ans:
        d2=nmap[w][a]
        if d1>=d2:
            wk.append(a)
            ans.remove(a)

# answer
for i in range(n):
    if i in ans:
        print("No")
    else:
        print("Yes")