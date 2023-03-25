n=int(input())

xlist=[]
ylist=[]
zlist=[]

for i in range(n):
    ab=input().split()
    a=int(ab[0])
    b=int(ab[1])
    xlist.append(a)
    ylist.append(b)
    zlist.append(a+b)

x1=min(xlist)
y1=min(ylist)
z1=min(zlist)
x2=sorted(xlist)[1]
y2=sorted(ylist)[1]

if xlist.index(x1) == ylist.index(y1):
    print(min(z1,max(x1,y2),max(x2,y1)))
else:
    print(max(x1,y1))
