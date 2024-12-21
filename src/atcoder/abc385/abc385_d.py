# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import bisect

# param
N,M,Sx,Sy = map(int, input().split())
XY=[]
for i in range(N):
    X,Y = map(int, input().split())
    XY.append([X,Y])
DC=[]
for i in range(M):
    D,C=input().split()
    DC.append([D,C])

xydict={}
yxdict={}
for X,Y in XY:
    if X not in xydict.keys():
        xydict[X]=[]
    xydict[X].append(Y)
    if Y not in yxdict.keys():
        yxdict[Y]=[]
    yxdict[Y].append(X)

# solve
ans=0
for i in range(M):
    D,C=DC[i]
    x=Sx
    y=Sy
    if D=="U":
        y+=int(C)
    elif D=="D":
        y-=int(C)
    elif D=="L":
        x-=int(C)
    elif D=="R":
        x+=int(C)
    if (D == "U" or D=="D") and x in xydict.keys():
        y1=min(y,Sy)
        y2=max(y,Sy)
        idx=[]
        idx.append(bisect.bisect_left(xydict[x],y1))
        idx.append(bisect.bisect_right(xydict[x],y2))
        ans+=idx[1]-idx[0]
        for wy in xydict[x][idx[0]:idx[1]]:
            yxdict[wy].remove(x)
        del xydict[x][idx[0]:idx[1]]
    if (D == "L" or D=="R") and y in yxdict.keys():
        x1=min(x,Sx)
        x2=max(x,Sx)
        idx=[]
        idx.append(bisect.bisect_left(yxdict[y],x1))
        idx.append(bisect.bisect_right(yxdict[y],x2))
        ans+=idx[1]-idx[0]
        for wx in yxdict[y][idx[0]:idx[1]]:
            xydict[wx].remove(y)
        del yxdict[y][idx[0]:idx[1]]
    Sx=x
    Sy=y
#    print("{} {}".format(Sx,Sy,ans))

# answer
print("{} {} {}".format(Sx,Sy,ans))
