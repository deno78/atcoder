# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
r,g,b = map(int, input().split())
c=input()

# solve
if c=='Red':
    print(min(g,b))
elif c=='Green':
    print(min(r,b))
elif c=='Blue':
    print(min(r,g))
