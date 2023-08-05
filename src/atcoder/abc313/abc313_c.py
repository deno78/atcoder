# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import math

# param
n = int(input())
alist=list(map(int,input().split()))

# solve
ans1a=0
ans2a=0
va=sum(alist)//n
if sum(alist)%n > n//2-1:
    va+=1
for i in range(n):
    a=alist[i]
    if a>va:
        ans1a+=a-va
    else:
        ans2a+=va-a
print(min(ans1a,ans2a))
