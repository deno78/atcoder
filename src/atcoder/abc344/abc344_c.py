# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int,input().split()))
m = int(input())
blist = list(map(int,input().split()))
l = int(input())
clist = list(map(int,input().split()))
q = int(input())
xlist = list(map(int,input().split()))

# solve
p=set([])
for a in alist:
    for b in blist:
        for c in clist:
            p.add(a+b+c)

# answer
for i in range(q):
    x=xlist[i]
    if x in p:
        print("Yes")
    else:
        print("No")
