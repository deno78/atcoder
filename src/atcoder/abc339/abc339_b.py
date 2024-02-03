# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w,n = map(int, input().split())

# solve
grid=[]
for i in range(h):
    grid.append(["."]*w)

dlist=[[0,-1],[1,0],[0,1],[-1,0]]
# dx=d%2 dy=d//2
d=0
x=0
y=0
for i in range(n):
#    print("[{}]{} {} {} {}".format(i,d,x,y,grid[y][x]))
    if grid[y][x]==".":
        grid[y][x]="#"
        d+=1
    else:
        grid[y][x]="."
        d-=1
    d%=4
    x+=dlist[d][0]
    y+=dlist[d][1]
    x%=w
    y%=h
#    print("[{}]{} {} {}".format(i,d,x,y))

# answer
for i in range(h):
    print("".join(grid[i]))