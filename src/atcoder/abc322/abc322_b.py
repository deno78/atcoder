# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
s = input()
t = input()

# solve
if t.startswith(s) and t.endswith(s):
    print(0)
elif t.startswith(s):
    print(1)
elif t.endswith(s):
    print(2)
else:
    print(3)

