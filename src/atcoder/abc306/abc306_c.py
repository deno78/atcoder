# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist=list(map(int,input().split()))

# solve
ans={}
for i in range(1,n+1):
    ans[i]=[]
for i in range(3*n):
    a=alist[i]
    ans[a].append(i)

ans2={}
for i in range(1,n+1):
    a=ans[i][1]
    ans2[a]=i

d = sorted(ans2.items())
p=[]
for v in d:
    p.append(str(v[1]))

# answer
print(" ".join(p))
