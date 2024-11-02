# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
qr=[]
for i in range(n):
    q, r = map(int,input().split())
    qr.append([q, r])
q = int(input())
td=[]
for i in range(q):
    t,d=map(int,input().split())
    t-=1
    td.append([t,d])

# solve
for i in range(q):
    t,d = td[i]
    q,r = qr[t]
    d2=d//q
    if d%q>r:
        d2+=1
    print(d2*q+r)


