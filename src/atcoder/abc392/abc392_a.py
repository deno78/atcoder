# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a1,a2,a3 = map(int, input().split())

# solve
if (a1*a2==a3) or (a2*a3==a1) or (a1*a3==a2):
    print("Yes")
else:
    print("No")
