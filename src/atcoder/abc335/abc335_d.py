# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

# solve
m=[]
for i in range(n):
    m.append([""]*n)
h=(n-1)//2
m[h][h]='T'

x=0
y=0
d=[[1,0],[0,1],[-1,0],[0,-1]]
idx=0
for i in range(1,n**2):
    m[y][x]=i
    dx=d[idx][0]
    dy=d[idx][1]
    x2=x+dx
    y2=y+dy
    if x2<0 or x2>=n or y2<0 or y2>=n or m[y2][x2]!="":
        idx=(idx+1)%len(d)
        dx=d[idx][0]
        dy=d[idx][1]
        x2=x+dx
        y2=y+dy
    x=x2
    y=y2

for l in m:
    l2=[]
    for i in l:
        l2.append(str(i))
    print(" ".join(l2))

# answer
