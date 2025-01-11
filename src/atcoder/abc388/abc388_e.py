# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import bisect

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
blist=[0]*n
for i in range(n):
    a=alist[i]
    x=a//2
    y=bisect.bisect_right(alist,x)
#    print("[{}]a:{} alist:{} pos:{}".format(i,a,alist,y))
    if y>0:
        ix=reversed(blist[0:y]).index(0)
        if ix>0:
            blist[i]=1
            blist[ix]=1

# answer
print(blist.count(1)//2)