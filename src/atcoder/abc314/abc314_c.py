# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
s = input()
clist=list(map(int,input().split()))
cdict={}
for i in range(m):
    cdict[i]=[]
for i in range(n):
    c=clist[i]
    cdict[c-1].append(i)

# solve
ans = [0]*n
for i in range(n):
    ans[i]=i

for i in range(m):
    if len(cdict[i])>0:
        tlist=cdict[i]
        alist=[]
        alist.append(ans[tlist[-1]])
        for j in range(len(tlist)-1):
            alist.append(ans[tlist[j]])
        for j in range(len(tlist)):
            t1=tlist[j]
            t2=alist[j]
            ans[t1]=t2
# answer
s2=[]
for a in ans:
    s2.append(s[a])
print("".join(s2))
