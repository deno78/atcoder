# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
s = input()

# solve
ans=[]
cnt=0
for i in range(n):
    if s[i]=="o" and cnt < k:
        ans.append("o")
        cnt+=1
    else:
        ans.append("x")

# answer
print("".join(ans))
