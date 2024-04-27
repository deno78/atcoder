# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def getVal(x,y):
    v=1
    if amap[y][x]!=".":
        v=amap[y][x]
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        x2=x+dx
        y2=y+dy
        if x2>=0 and x2<w and y2>=0 and y2<h and amap[y2][x2]!="." and amap[y2][x2]!="#":
            v+=amap[y2][x2]
    return v


# param
h,w = map(int, input().split())
amap=[]
for i in range(h):
    amap.append(list(input()))

# solve
wk=[]
for y in range(h):
    for x in range(w):
        if amap[y][x]=="#":
            for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                x2=x+dx
                y2=y+dy
                if x2>=0 and x2<w and y2>=0 and y2<h and amap[y2][x2]==".":
                    wk.append([x2,y2])
                    amap[y2][x2]=1

ans=1
while len(wk)>0:
    xy=wk.pop(0)
    x1=xy[0]
    y1=xy[1]
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        x2=x1+dx
        y2=y1+dy
        if x2>=0 and x2<w and y2>=0 and y2<h:
            if amap[y2][x2]==".":
                amap[y2][x2]=amap[y1][x1]+1
                ans=max(ans,amap[y2][x2])
                wk.append([x2,y2])

print(amap)
print(ans)