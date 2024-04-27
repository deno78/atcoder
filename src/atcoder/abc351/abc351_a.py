# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

# solve
ans = max(0,sum(alist)-sum(blist)+1)

# answer
print("{}".format(ans))
