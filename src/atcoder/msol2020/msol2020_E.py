n = int(input(''))

xyplist = []
xlist=[]
ylist=[]
for i in range(n):
    xyp = list(map(int,input().split()))
    xyplist.append(xyp)
    xlist.append(xyp[0])
    ylist.append(xyp[1])

for i in range(n):
    cost=0
    for xyp in xyplist:
        x=xyp[0]
        y=xyp[1]
        p=xyp[2]
        if x<y:
            cost+=p*x
        else:
            cost+=p*y
