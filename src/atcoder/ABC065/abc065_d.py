n=int(input())


xylist=[]
for i in range(n):
    xy = list(map(int,input().split()))
    d=min(abs(xy[0]),abs(xy[1]))
    xy.insert(0,d)
    xylist.append(xy)

xylist.sort()
print(xylist)
m=0

