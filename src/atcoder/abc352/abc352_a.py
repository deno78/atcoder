# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,x,y,z = map(int, input().split())

# solve
if (x<y and x<z and z<y) or (x>y and x>z and z>y):
    print("Yes")
else:
    print("No")