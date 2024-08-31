# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a,b = map(int, input().split())

# solve
if a==b:
    print(1)
elif abs(a-b)%2==0 and abs(a-b)>1:
    print(3)
else:
    print(2)
