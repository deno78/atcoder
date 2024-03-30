# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,a,b = map(int, input().split())
dlist = list(map(int, input().split()))

# solve
ans=[]
for i in range(n):
    d=(dlist[i]-dlist[0])%(a+b)
    if d>a:
        ans.append(d-a-b)
    else:
        ans.append(d)

if abs(max(ans)-min(ans))<a:
    print("Yes")
else:
    print("No")