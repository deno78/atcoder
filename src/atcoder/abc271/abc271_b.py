# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int,input().split())
alist=[]
for i in range(n):
    a=list(map(int,input().split()))[1:]
    alist.append(a)
qlist=[]
for i in range(q):
    qlist.append(list(map(int,input().split())))

# solve
for i in range(q):
    s,t=qlist[i]
    print(alist[s-1][t-1])