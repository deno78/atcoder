h,w=map(int,input().split())

amap=[]
for i in range(h):
    amap.append(list(input()))
bmap=[]
for i in range(h):
    bmap.append(list(input()))


for s in range(h):
    for t in range(w):
        ok=True
        for x in range(h):
            for y in range(w):
                x2=(x+s)%h
                y2=(y+t)%w
                if amap[x2][y2]!=bmap[x][y]:
                    ok=False
                    break
            if ok == False:
                break
        if ok:
            print("Yes")
            exit()

print("No")
                
