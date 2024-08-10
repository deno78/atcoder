# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,t,a = map(int, input().split())

# solve
# answer
if t > n//2 or a > n//2:
    print("Yes")
else:
    print("No")