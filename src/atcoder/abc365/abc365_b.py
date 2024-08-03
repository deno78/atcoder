# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

adict={}
for i in range(n):
    a=alist[i]
    adict[a]=i

alist.sort()
# solve
ans = adict[alist[-2]]

# answer
print("{}".format(ans+1))
