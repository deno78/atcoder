# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
r=[]
for i in range(n):
    r.append([float("INF")]*n)

for i in range(n-1):
    a,b,c = map(int, input().split())
    a-=1
    b-=1
    r[a][b]=c
    r[b][a]=c

# solve
s1=-1
s2=-1
max_cost=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                r[i][j]=0
            else:
                r[i][j]=min(r[i][j],r[i][k]+r[k][j])
                if r[i][j]>max_cost:
                    max_cost=r[i][j]
                    s1=i
                    s2=j


wk=[]
wk.append([s1])

while len(wk)>0:
    w=wk.pop(0)
    