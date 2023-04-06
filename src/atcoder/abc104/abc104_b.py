# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
if s[0]!="A":
    print("WA")
    exit()
elif s[2:-2].count("C")!=1:
    print("WA")
    exit()
else:
    for c in s:
        if c in "BDEFGHIJKLMNOPQRSTUVWXYZ":
            print("WA")
            exit()

print("AC")