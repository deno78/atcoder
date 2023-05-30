# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=[]
for i in range(m):
    alist.append(list(map(int,input().split())))

adict={}
for i in range(n):
    adict[i]=[]


for i in range(m):
    for j in range(1,n):
        a1=alist[i][j-1]-1
        a2=alist[i][j]-1
        adict[a1].append(a2)
        adict[a2].append(a1)
ans=0
for i in range(n):
    acnt=len(list(set(adict[i])))
    ans+=(n-acnt-1)

print(ans//2)