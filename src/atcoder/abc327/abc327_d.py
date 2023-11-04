# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

for i in range(m):
    if alist[i]==blist[i]:
        print("No")
        exit()

# solve
chk=[-1]*n
for i in range(m):
    a=alist[i]-1
    b=blist[i]-1
    if chk[a]!=-1 and chk[b]!=-1 and chk[a]==chk[b]:
        print("No")
        exit()
    if chk[a]==-1:
        chk[a]=0
    elif chk[a]==0:
        chk[b]=1
    elif chk[a]==1:
        chk[b]=0
    if chk[b]==-1:
        chk[b]=0
    elif chk[b]==0:
        chk[a]=1
    elif chk[b]==1:
        chk[a]=0

# answer
print("Yes")
