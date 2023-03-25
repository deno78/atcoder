h,w=map(int,input().split())

map=[]
for i in range(h):
    map.append(list(input()))

map2=[]
for i in range(h):
    map2.append([])
    for j in range(w):
        if map[i][j]==".":
            map2[i].append(0)
        else:
            map2[i].append(-1)
d=0
pos=[]
pos.append([0,0])
while len(pos)>0:
    print(pos)
    for x,y in pos:
        for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            x2=x+dx
            y2=y+dy
            if x2>=0 and x2<h and y2>=0 and y2<w:
                if map2[x2][y2]==-1:
                    map2[x2][y2]=d+1
                    pos.append([x2,y2])
        pos.pop(0)
for r in map2:
    print(r)