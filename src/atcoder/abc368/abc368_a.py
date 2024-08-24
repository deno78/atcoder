# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k = map(int, input().split())
alist = list(map(int, input().split()))

# solve
for i in range(k):
    a=alist.pop(-1)
    alist.insert(0,a)

# answer
alist2=[]
for a in alist:
    alist2.append(str(a))
print(" ".join(alist2))
