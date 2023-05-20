# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a,b = map(int, input().split())

# solve
if a%b==0:
    print(a//b)
else:
    print(a//b+1)
