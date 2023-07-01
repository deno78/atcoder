# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s=list(map(int,input().split()))

# solve
for i in range(1,len(s)):
    if s[i]<s[i-1]:
        print("No")
        exit()
for i in range(len(s)):
    if s[i]<99 or s[i]>676:
        print("No")
        exit()
    if s[i]%25!=0:
        print("No")
        exit()

# answer
print("Yes")