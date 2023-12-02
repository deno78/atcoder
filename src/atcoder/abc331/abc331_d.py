# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int, input().split())
pmap=[]
for i in range(n):
    pmap.append(list(input()))
qlist=[]
for i in range(q):
    qlist.append(list(map(int,input().split())))

# solve
pmap2=[]
for i in range(n):
    pmap2.append([0]*n)

if pmap[0][0]=="B":
    pmap2[0][0]=1

w=0
for i in range(n):
    if pmap[0][i]=="B":
        w+=1
    pmap2[0][i]=w
for i in range(1,n):
    w=0
    for j in range(n):
        if pmap[i][j]=="B":
            w+=1
        pmap2[i][j]=pmap2[i-1][j]+w

for p in pmap2:
    print(p)
# answer
for i in range(q):
    a,b,c,d=qlist[i]
    a1=a%n
    a2=a//n
    a3=n-a%n
    w=0
    for j in range(d-b):
        w+=pmap[j][c]-pmap[j][a]
    print(w)


