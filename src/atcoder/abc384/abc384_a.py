# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,c1,c2 = input().split()
s = input()
n=int(n)

# solve
ans=[]
for i in range(n):
    if s[i]==c1:
        ans.append(s[i])
    else:
        ans.append(c2)

# answer
print("".join(ans))
