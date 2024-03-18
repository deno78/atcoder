# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
# answer
s2=set(list(s[1:-1]))
if s[0]=="<" and s[-1]==">" and len(s2)==1 and "=" in s2:
    print("Yes")
else:
    print("No")