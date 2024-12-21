# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a,b, c = map(int, input().split())

# solve
if a+b==c or b+c==a or a+c==b or (a==b and b==c):
    print("Yes")
else:
    print("No")
