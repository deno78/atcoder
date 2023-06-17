# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from bisect import bisect
import heapq

# param
n,k,q = map(int, input().split())
xy=[]
for i in range(q):
    x,y=map(int,input().split())
    xy.append([x-1,y])

alist=[0]*n
blist=[]
# solve
for i in range(q):
    x,y=xy[i]
    pa=alist[x]
    if pa!=0:
        blist.remove(pa)
    alist[x]=y
    blist.insert(bisect(blist,y),y)
    print(sum(blist[-1*k:]))

