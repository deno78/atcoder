n=int(input())
udlr=[]
for i in range(n):
    udlr.append(list(map(int,input().split())))

xset=set()
yset=set()
for u,d,l,r in udlr:
    xset.add(l)
    xset.add(r)
    yset.add(u)
    yset.add(d)
xlist=sorted(list(xset))
ylist=sorted(list(yset))
xlist.insert(0,0)
ylist.insert(0,0)
print(xlist)
print(ylist)
grid=[]
for i in range(len(ylist)):
    grid.append([0]*len(xlist))

all=2000*2000
for i in range(n):
    u,d,l,r=udlr[i]
    li=xlist.index(l)
    ri=xlist.index(r)+1
    ui=ylist.index(u)
    di=ylist.index(d)+1
    for j in range(ui,di):
        for k in range(li,ri):
            if grid[j][k]==0:
                w=xlist[k]-xlist[k-1]
                h=ylist[j]-ylist[j-1]
                print(f"i:{i} x:{xlist[k-1]}-{xlist[k]},y:{ylist[j-1]}-{ylist[j]},w:{w},h:{h}")
                all-=w*h
            grid[j][k]+=1

for g in grid:
    print(g)

for i in range(n):
    u,d,l,r=udlr[i]
    li=xlist.index(l)
    ri=xlist.index(r)+1
    ui=ylist.index(u)
    di=ylist.index(d)+1
    ans=0
    for j in range(ui,di):
        for k in range(li,ri):
            if grid[j][k]==1:
                w=xlist[k]-xlist[k-1]
                h=ylist[j]-ylist[j-1]
                ans+=w*h
    print(all+ans)
