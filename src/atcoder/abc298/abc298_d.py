# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
q = int(input())
s=[]
s.append("1")
d=0
for _ in range(q):
    p = input().split()
#    print("{}:{}".format(p[0],s))
    if p[0]=="1":
        s.append(p[1])
    elif p[0]=="2":
        d+=1
    elif p[0]=="3":
        s=s[d:]
        d=0
        s2=int("".join(s))
        print(int(s2)%998244353)
