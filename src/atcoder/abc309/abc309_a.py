# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a,b = map(int, input().split())
a-=1
b-=1

# solve
if a//3 == b//3:
    if abs(a%3-b%3)==1:
        print("Yes")
        exit()
print("No")

