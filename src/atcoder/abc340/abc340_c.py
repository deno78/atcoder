# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import math

# param
n = int(input())

# solve
ans = 0

o=0
e=0
ox=n
ex=n
if n%2==0:
    ex=n
    ox=n+1
    e=1
else:
    ox=n
    ex=n-1
    e=1

print("{}:{} {}:{}".format(ex,e,ox,o))                

while ox>1 or ex>1:
    o2=0
    e2=0
    e=e//2
    if ox%2==0:
        e2+=o*2
    else:
        e2+=o
        o2+=o
    if ex%2==0:
        e2+=e*2
    else:
        o2+=e
        e2+=e
    if ex%2==0:
        ex=ex//2
        ox=ex+1
    else:
        ox=ex//2+1
        ex=ex//2
    e=e2
    o=o2
    ans+=n
    if 
    print("{}:{} {}:{} {}".format(ex,e,ox,o,ans))                


# answer
print("{}".format(ans))
