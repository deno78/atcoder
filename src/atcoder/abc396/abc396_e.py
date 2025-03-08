# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
xlist=[]
ylist=[]
zlist=[]
for i in range(m):
    x,y,z = map(int, input().split())
    xlist.append(x)
    ylist.append(y)
    zlist.append(z)

alist=[-1]*n

for i in range(m):
    x=xlist[i]
    y=ylist[i]
    z=zlist[i]
    if alist[x]>-1:
        ax=alist[x]
    if alist[y]>-1:
        ay=alist[y]
    if alist[x]>-1 and alist[y]>-1:
        

# solve
ans = a + b + c

# answer
print("{} {}".format(ans, s))
