n,m,x,y=map(int,input().split())
xlist=list(map(int,input().split()))
ylist=list(map(int,input().split()))
xlist.append(x)
ylist.append(y)
#print("X:{} Y:{}".format(max(xlist),min(ylist)))
if max(xlist)>min(ylist)-1:
    print("War")
else:
    print("No War")