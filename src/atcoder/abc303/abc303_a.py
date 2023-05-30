# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
s = input()
t = input()

# solve

# answer
for i in range(n):
    if s[i]==t[i] or (s[i] in ["1","l"] and t[i] in ["1","l"]) or (s[i] in ["0","o"] and t[i] in ["0","o"]):
        pass
    else:
        print("No")
        exit(0)

print("Yes")
