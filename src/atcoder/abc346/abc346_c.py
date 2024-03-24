# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
alist= list(map(int, input().split()))

# solve
ans = k*(k+1)//2
aset=list(set(alist))
for a in aset:
    if a<=k:
        ans-=a

# answer
print("{}".format(ans))
