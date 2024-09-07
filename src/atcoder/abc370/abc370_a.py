# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
l,r = map(int, input().split())

# solve
if l==1 and r==0:
    print("Yes")
elif l==0 and r==1:
    print("No")
elif l==1 and r==1:
    print("Invalid")
elif l==0 and r==0:
    print("Invalid")