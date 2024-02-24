# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ans=0
if s[0]!=s[1] and s[0]!=s[2]:
    print(1)
else:
    for i in range(len(s)):
        if s[0]!=s[i]:
            print(i+1)
            exit()
