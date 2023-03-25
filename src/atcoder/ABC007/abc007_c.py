from collections import deque

rc = input('').split()
r = int(rc[0])
c = int(rc[1])

syx = list(map(int,input('').split()))
gyx = list(map(int,input('').split()))

cell=[]
for i in range(r):
    cell.append(input(''))

ans=[]
for i in range(r):
    ans.append([0]*c)

y=syx[0]-1
x=syx[1]-1
gy=gyx[0]-1
gx=gyx[1]-1
ans[x][y]=0
q = deque()

def draw(cell,ans,x,y,val):
    if cell[y][x]=='.' and ans[y][x]==0:
        ans[y][x]=val+1
    return ans

def func(cell,ans,x,y,q):
    if y <0 or x < 0 or y > len(cell) or y > len(cell[0]):
        return ans

    if cell[y][x] == "#":
        return ans
    val=ans[y][x]
    q.append([y,x])
    ans = draw(cell,ans,x,y+1,val)
    ans = draw(cell,ans,x,y-1,val)
    ans = draw(cell,ans,x+1,y,val)
    ans = draw(cell,ans,x-1,y,val)

#    for i in ans: print("".join(str(i)))

    if [y+1,x] not in q:
        ans = func(cell,ans,x,y+1,q)
    if [y-1,x] not in q:
        ans = func(cell,ans,x,y-1,q)
    if [y,x+1] not in q:
        ans = func(cell,ans,x+1,y,q)
    if [y,x-1] not in q:
        ans = func(cell,ans,x-1,y,q)
    return ans

ans = func(cell,ans,x,y,q)
#for i in ans: print("".join(str(i)))
print(ans[gy][gx])