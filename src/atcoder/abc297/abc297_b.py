# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
r1=-1
k=-1
r2=-1
x=-1
y=-1
for i in range(len(s)):
    if r1==-1 and s[i]=="R":
        r1=i
    elif r1!=-1 and r2==-1 and s[i]=="R":
        r2=i
    elif s[i]=="K":
        k=i
    elif x==-1 and s[i]=="B":
        x=i
    elif x!=-1 and y==-1 and s[i]=="B":
        y=i
if r1 < k and k < r2 and x%2!=y%2:
    print("Yes")
else:
    print("No")