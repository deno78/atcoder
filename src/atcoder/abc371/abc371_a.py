# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s=input().split()
s=" ".join(s)

# solve
if s=="< < <":
    print("B") # ABC
elif s=="< < >":
    print("C") # ACB
elif s=="< > <":
    print("A") # CAB
elif s=="< > >":
    print("A") # CAB
elif s=="> < <":
    print("A") # BAC
elif s=="> < >":
    print("A") # BAC
elif s=="> > <":
    print("C") # BCA
elif s=="> > >":
    print("B") # CBA
