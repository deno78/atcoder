# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
M,D = map(int, input().split())
y,m,d = map(int, input().split())

# solve
if d==D and M==m:
    print("{} {} {}".format(y+1,1,1))
elif d==D:
    print("{} {} {}".format(y,m+1,1))
else:
    print("{} {} {}".format(y,m,d+1))
