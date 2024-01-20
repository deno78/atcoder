# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
xa=0
ya=0
for i in range(n):
    x,y = map(int, input().split())
    xa+=x
    ya+=y

# solve

# answer
if xa>ya:
    print("Takahashi")
elif xa<ya:
    print("Aoki")
else:
    print("Draw")