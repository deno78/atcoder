# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m,p = map(int, input().split())

# solve
if m>n:
    print(0)
    exit()

ans = (n-m)//p+1

# answer
print("{}".format(ans))
