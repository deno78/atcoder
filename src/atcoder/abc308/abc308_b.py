# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
clist=input().split()
dlist=input().split()
plist=list(map(int,input().split()))

ddic={}
for i in range(m):
    d=dlist[i]
    p=plist[i+1]
    ddic[d]=p

# solve
ans = 0

for i in range(n):
    c=clist[i]
    if c in ddic.keys():
        ans+=ddic[c]
    else:
        ans+=plist[0]

# answer
print(ans)