# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def l(s):
    ls=list(s)
    ls.sort()
    if "".join(ls) in ["AB","BC","CD","DE","AE"]:
        return 1
    else:
        return 2

# param
s1 = list(input())
s2 = list(input())

l1=l(s1)
l2=l(s2)

# answer
if l1==l2:
    print("Yes")
else:
    print("No")
