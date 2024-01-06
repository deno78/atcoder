# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

# solve
for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            if i+j+k<=n:
                print("{} {} {}".format(i,j,k))

