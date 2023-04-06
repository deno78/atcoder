# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()

# solve
for i in range(1,n):
    if s[i-1]==s[i]:
        print("No")
        exit()

print("Yes")
