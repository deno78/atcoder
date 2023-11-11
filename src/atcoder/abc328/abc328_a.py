# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,x = map(int, input().split())
slist = list(map(int, input().split()))

# solve
ans=0
for i in range(n):
    if slist[i]<=x:
        ans+=slist[i]

# answer
print("{}".format(ans))
