# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a = int(input())

# solve
ans = ("0" + hex(a)[2:])[-2:].upper()

# answer
print(ans)
