# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h = int(input())

# solve
d=0
x=0
while True:
    x+=2**d
    d+=1
    if x>h:
        print(d)
        exit()

