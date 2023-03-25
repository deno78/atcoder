h,w=map(int,input().split())

amap=[]
for i in range(h):
    amap.append(list(input()))

amap2=[]
for a in amap:
    if "#" in a:
        amap2.append(a)
amap=amap2

amap2=[]
for y in range(len(amap)):
    amap2.append([])

for x in range(len(amap[0])):
    same=True
    for y in range(len(amap)):
#        print("[{},{}={}] / [{},{}={}]".format(x,y,amap[y][x],0,y,amap[0][x]))
        if amap[y][x]=="#":
            same=False
    if not same:
        for y in range(len(amap)):
            amap2[y].append(amap[y][x])
amap=amap2

for a in amap:
    print("".join(a))
