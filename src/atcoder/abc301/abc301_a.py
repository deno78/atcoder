# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()

# solve
a1=s.count("T")
a2=s.count("A")
if a1==a2:
    for i in range(n):
        if s[:i].count("T")>=n//2:
            print("T")
            exit()
        elif s[:i].count("A")>=n//2:
            print("A")
            exit()
elif a1>a2:
    print("T")
    exit()
elif a1<a2:
    print("A")
    exit()
