from collections import deque

h,w=map(int,input().split())
grid=[list(input()) for _ in range(h)] 


wk=deque([])
for y in range(h):
    for x in range(w):
        if grid[y][x]=="#":
            wk.append([x,y,0])

ans=len(wk)
directions=[[1,0],[-1,0],[0,1],[0,-1]]
while len(wk)>0:
    x,y,d=wk.popleft()
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<w and 0<=ny<h and grid[ny][nx]==".":
            cnt=0
            for dx,dy in directions:
                nnx,nny=nx+dx,ny+dy
                if 0<=nnx<w and 0<=nny<h:
                    if grid[nny][nnx]=="#":
                        cnt+=1
                    elif grid[nny][nnx]==".":
                        continue
                    else:
                        dx=grid[nny][nnx]
                        if dx<=d:
                            cnt+=1
            if cnt==1:
                grid[ny][nx]=d+1
                wk.append([nx,ny,d+1])
                ans+=1

#    print(g)
print(ans)

