# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist = list(map(int, input().split()))

alist.sort()

# solve
blist=[]
for i in range(1,n+1):
    if i not in alist:
        blist.append(str(i))

# answer
print(len(blist))
print(" ".join(blist))