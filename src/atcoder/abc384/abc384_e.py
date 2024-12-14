# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w,a = map(int, input().split())
q,p = map(int, input().split())
p-=1
q-=1

grid=[]
for i in range(h):
    slist = list(map(int, input().split()))
    grid.append(slist)
# solve
wk=[]
wk.append([p,q])

ans=grid[q][p]
grid[q][p]=-1
while len(wk)>0:
    z=wk.pop(0)
    ok=False
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        x=z[0]+dx
        y=z[1]+dy
        if 0<=x and x<w and 0<=y and y<h:
            pw=grid[y][x]
#            print("[{},{}]={} => {}/{}".format(x,y,pw,a*pw,ans))
            if a*pw<ans and grid[y][x]!=-1:
                ans+=pw
                wk.append([x,y])
                ok=True
                grid[y][x]=-1
    if ok:
        wk.append(z)

# answer
print("{}".format(ans))
