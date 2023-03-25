h,w=map(int,input().split())

blacks=[]
map=[]
for i in range(h):
    map.append(list(input()))
map2=[]

for i in range(h):
    map2.append([])
    for j in range(w):
        if map[i][j]=='#':
            blacks.append([i,j])
            map2[i].append(0)
        else:
            map2[i].append(-1)

ans=0
while len(blacks)< h*w:
    for b in blacks:
        x1=b[0]
        y1=b[1]
        d=map2[x1][y1]
        for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            x=b[0]+dx
            y=b[1]+dy
            if x>=0 and x<h and y>=0 and y<w and map2[x][y]== -1:
                map2[x][y]=d+1
                blacks.append([x,y])
                ans=max(ans,d+1)

print(ans)
