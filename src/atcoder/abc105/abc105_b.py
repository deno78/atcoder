# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

# solve
for i in range(n//4+1):
    for j in range(n//7+1):
        if i*4+j*7==n:
            print("Yes")
            exit()

# answer
print("No")