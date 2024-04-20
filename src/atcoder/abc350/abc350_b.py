# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int, input().split())
tlist = list(map(int, input().split()))

# solve
ans=[1]*n

for t in tlist:
    t-=1
    if ans[t]==1:
        ans[t]=0
    elif ans[t]==0:
        ans[t]=1

# answer
print(ans.count(1))
