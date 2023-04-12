# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
if s[0]!="A":
    print("WA")
    exit()
elif s[2:-1].count("C")!=1:
    print("WA")
    exit()
else:
    c_idx=s.index("C")
    for i in range(1,c_idx):
        c = s[i]
#        print("[{}] {}".format(i,c))
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("WA")
            exit()
    for i in range(c_idx+1,len(s)):
        c = s[i]
#        print("[{}] {}".format(i,c))
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("WA")
            exit()

print("AC")