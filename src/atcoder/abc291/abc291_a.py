# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
for i in range(len(s)):
    c=s[i]
    if c!= c.lower():
        print(i+1)
        exit()

