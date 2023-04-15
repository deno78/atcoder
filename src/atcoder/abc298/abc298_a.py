# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()

# solve
good=False
bad=False

for c in list(s):
    if c=="o":
        good=True
    elif c=="x":
        bad=True

# answer
if good and not bad:
    print("Yes")
else:
    print("No")
