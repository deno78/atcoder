# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
ans = []

for i in range(len(s)//2):
    ans.append(s[2*i+1])
    ans.append(s[2*i])

# answer
print("".join(ans))
