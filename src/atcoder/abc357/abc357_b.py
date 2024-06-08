# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
u=0
l=0
for i in range(len(s)):
    c=s[i]
    if c.isupper():
        u+=1
    else:
        l+=1
if u>l:
    print(s.upper())
else:
    print(s.lower())

