# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

# solve
while n%2==0:
    n=n//2

while n%3==0:
    n=n//3

if n==1:
    print("Yes")
else:
    print("No")