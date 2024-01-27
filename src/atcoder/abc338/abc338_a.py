# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve

if s[0].isupper():
    for i in range(1,len(s)):
        
        if s[i].isupper():
            print("No")
            exit()
    print("Yes")
    exit()
else:
    print("No")
    exit()
