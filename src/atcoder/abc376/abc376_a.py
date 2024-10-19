# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,c = map(int, input().split())
tlist = list(map(int, input().split()))

# solve
ans = 1
x=tlist[0]
for i in range(1,n):
    if tlist[i]-x>=c:
        ans+=1
        x=tlist[i]


# answer
print("{}".format(ans))
