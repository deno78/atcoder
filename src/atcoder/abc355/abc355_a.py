# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
a,b = map(int, input().split())

# solve
ans=[]
for i in range(1,4):
    if i!=a and i!=b:
        ans.append(i)

# answer
if len(ans)==1:
    print(ans[0])
else:
    print(-1)