# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
alist=list(map(int,input().split()))

# solve
ans = 0
for i in range(len(alist)):
    ans+=alist[i]*2**i


# answer
print("{}".format(ans))
