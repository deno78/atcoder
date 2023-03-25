import math
import statistics

n=int(input())
alist=list(map(int,input().split()))
if n==2:
    print("{} {}".format(alist[0],alist[1]))
    exit()

alist.sort()

a=alist[-1]
b=alist[n//2]
print("{} {}".format(a,b))

