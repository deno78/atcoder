# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ac=s.count("A")
bc=s.count("B")
cc=s.count("C")
a2=["A"]*ac
b2=["B"]*bc
c2=["C"]*cc
s2="".join(a2)+"".join(b2)+"".join(c2)

if s==s2:
    print("Yes")
else:
    print("No")
