# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
ab=[]
for i in range(m):
    a,b=map(int,input().split())
    ab.append([a,b])

# solve
chk=[]
for i in range(n):
    chk.append(i+1)

for a,b in ab:
    if b in chk:
        chk.remove(b)

# answer
if len(chk)==1:
    print(chk[0])
else:
    print(-1)
