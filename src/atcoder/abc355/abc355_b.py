# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

cdict={}
clist=[]
for a in alist:
    cdict[a]='A'
    clist.append(a)
for b in blist:
    cdict[b]='B'
    clist.append(b)

clist.sort()

for i in range(1,len(clist)):
    c1=clist[i-1]
    c2=clist[i]
    if cdict[c1]=="A" and cdict[c2]=="A":
        print("Yes")
        exit()

# solve
print("No")