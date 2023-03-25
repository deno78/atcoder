import numpy as np
import math
# TODO edit this code


def check(x1,y1,x2,y2,x3,y3):
    a=np.array([x1,y1])
    b=np.array([x2,y2])
    c=np.array([x3,y3])
    va=a-b
    vc=c-b
    lva=np.linalg.norm(va)
    lvc=np.linalg.norm(vc)
    ip=np.inner(va,vc)
    cos=ip/(lva*lvc)
    rad=np.arccos(cos)
    deg=np.rad2deg(rad)
    return deg

# param
ax,ay=map(int,input().split())
bx,by=map(int,input().split())
cx,cy=map(int,input().split())
dx,dy=map(int,input().split())

# solve
r1=check(ax,ay,bx,by,cx,cy)
r2=check(bx,by,cx,cy,dx,dy)
r3=check(cx,cy,dx,dy,ax,ay)
r4=check(dx,dy,ax,ay,bx,by)


# answer
if r1+r2+r3+r4 >=359:
    print('Yes')
else:
    print('No')
