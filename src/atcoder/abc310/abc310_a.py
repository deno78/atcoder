# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,p,q = map(int, input().split())
dlist=list(map(int,input().split()))

# solve
print(min(p,q+min(dlist)))
