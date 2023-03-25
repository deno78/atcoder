from operator import mul
from functools import reduce
import itertools

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n=int(input())
xylist=[]        
xyset=[]
for i in range(n):
    x,y=map(int,input().split())
    xylist.append([x,y])
    xyset.append("{}-{}".format(x,y))

cnt=0
for xy1,xy2 in itertools.combinations(xylist,2):
    x1=xy1[0]
    x2=xy2[0]
    y1=xy1[1]
    y2=xy2[1]
    xy3="{}-{}".format(x1,y2)
    xy4="{}-{}".format(x2,y1)
    if xy3 in xyset and xy4 in xyset:
        print(xy3 + "/" + xy4)
        cnt+=1

print(cnt)

