# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import bisect

# param
n = int(input())
alist = list(map(int, input().split()))
alist.sort()

# solve
ans = 0
for i in range(n):
    a=alist[i]
    x=a//2
    y=bisect.bisect_right(alist,x)
#    print("[{}]a:{} alist:{} pos:{}".format(i,a,alist,y))
    if y>0:
        ans+=(y)

# answer
print("{}".format(ans))
