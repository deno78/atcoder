# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a,m,l,r = map(int, input().split())

# solve
d=a%m
l-=d
r-=d
if r==l:
    print(0)
else:
    print((r-l)//m+1)