from collections import deque

h,w=map(int,input().split())
smap=[]
#cmap=[]
starts=[]
for i in range(h):
    l=list(input())
    smap.append(l)
#    cmap.append([float("INF")]*w)
    for j in range(w):
        if l[j]=="E":
            starts.append([i,j])
#            cmap[i][j]=0

wk=deque(starts)

direction=[[-1,0],[1,0],[0,-1],[0,1]]
arrows=["v","^",">","<"]

while len(wk)>0:
    x=wk.popleft()
#    c=cmap[x[0]][x[1]]
    for i in range(len(direction)):
        d=direction[i]
        next_y=x[0]+d[0]
        next_x=x[1]+d[1]
        if 0<=next_y<h and 0<=next_x<w and smap[next_y][next_x]==".":
            smap[next_y][next_x]=arrows[i]
#                cmap[next_y][next_x]=c+1
            wk.append([next_y,next_x])

for l in smap:
    print("".join(l))