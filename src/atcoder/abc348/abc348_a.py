# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

# solve
ans=[]
for i in range(1,n+1):
    if i%3==0:
        ans.append("x")
    else:
        ans.append("o")
print("".join(ans))