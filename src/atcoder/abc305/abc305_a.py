# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

# solve
if n%5> 2.5:
    ans = (n//5+1) *5
else:
    ans = (n//5) *5

# answer
print("{}".format(ans))
