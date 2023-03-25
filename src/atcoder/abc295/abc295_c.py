# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist=list(map(int,input().split()))

# solve
ans=0
p={}
for i in range(n):
    a=alist[i]
    if a not in p.keys():
        p[a]=1
    elif a in p.keys():
        if p[a]==1:
            ans+=1
            p[a]=0
        else:
            p[a]=1

# answer
print(ans)