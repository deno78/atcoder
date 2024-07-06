# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,k,x = map(int, input().split())
alist = list(map(int, input().split()))

# solve
alist.insert(k,x)
blist=[]
for i in range(len(alist)):
    blist.append(str(alist[i]))

# answer
print(" ".join(blist))
