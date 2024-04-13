# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()
t = input()
t=t.lower()
# solve
i2=0

for i in range(len(s)):
    if i2==3:
        break
    if s[i]==t[i2]:
        i2+=1
# answer
if i2==2 and t[2]=="x":
    print("Yes")
elif i2==3:
    print("Yes")
else:
    print("No")
