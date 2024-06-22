# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))

# solve
ans = 0
for i in range(n*2-2):
    a1=alist[i]
    a2=alist[i+2]
    if a1==a2:
        ans+=1

# answer
print("{}".format(ans))
