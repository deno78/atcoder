# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
x = int(input())
ans=0
for i in range(1,10):
    for j in range(1,10):
        if i*j!=x:
            ans+=i*j

# solve

# answer
print("{}".format(ans))
