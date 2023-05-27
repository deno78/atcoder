# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m,h,k = map(int, input().split())
s = input()
xy={}
for i in range(m):
    dx,dy=map(int,input().split())
    if dx not in xy.keys():
        xy[dx]=[]
    xy[dx].append(dy)

x=0
y=0

for i in range(n):
    c=s[i]
    if c=="R":
        x+=1
    elif c=="L":
        x-=1
    elif c=="U":
        y+=1
    elif c=="D":
        y-=1
    h-=1
    if h<0:
        print("No")
        exit()
    if h<k and x in xy.keys() and y in xy[x]:
        h=k
        xy[x].remove(y)

if h<0:
    print("No")
    exit()
print("Yes")