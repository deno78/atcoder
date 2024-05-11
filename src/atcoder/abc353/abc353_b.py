# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
alist = list(map(int, input().split()))

# solve
ans=0
wk=0
for i in range(n):
    if wk+alist[i]>k:
        ans+=1
        wk=alist[i]
    else:
        wk+=alist[i]

if wk>0:
    ans+=1

# answer
print("{}".format(ans))
