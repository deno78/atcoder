# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,a = map(int, input().split())
tlist=list(map(int, input().split()))

# solve
ans = []
x=0
for i in range(n):
    t=tlist[i]
    if t>x:
        x=t+a
    else:
        x=x+a
    ans.append(str(x))

# answer
for a in ans:
    print(a)
