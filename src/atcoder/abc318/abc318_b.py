# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
abcd=[]
for i in range(n):
    a,b,c,d = map(int, input().split())
    a-=1
    b-=1
    c-=1
    d-=1
    abcd.append([a,b,c,d])

# solve
m=[]
for i in range(101):
    m.append([0]*101)

for a,b,c,d in abcd:
    for x in range(a,b):
        for y in range(c,d):
            m[x][y]+=1

ans=0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]>0:
            ans+=1

# answer
print("{}".format(ans))
