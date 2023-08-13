# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
clist=[]
aclist=[]
adict={}
for i in range(37):
    adict[i]=[]

for i in range(n):
    c = int(input())
    alist=list(map(int, input().split()))
    clist.append(c)
    aclist.append(alist)
    for a in alist:
        adict[a].append(i)
x = int(input())

# solve
m=float("INF")
for i in adict[x]:
    m=min(m,clist[i])
ans=[]
for i in adict[x]:
    if clist[i]==m:
        ans.append(i)
ans.sort()
# answer
ans2=[]
for a in ans:
    ans2.append(str(a+1))
print(len(ans2))
print(" ".join(ans2))