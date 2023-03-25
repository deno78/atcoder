import sys
sys.setrecursionlimit(10000)

def fnc(start,pos):
    for to in dlist[pos]:
        if to not in ans[start]:
            ans[start].append(to)
            fnc(start,to)

nm=input().split()
n=int(nm[0])
m=int(nm[1])

dlist={}
for i in range(n):
    dlist[i]=[]

ans={}
for i in range(n):
    ans[i]=[]
    ans[i].append(i)

for i in range(m):
    ab=list(map(int,input().split()))
    a=ab[0]-1
    b=ab[1]-1
    dlist[a].append(b)

for i in range(n):
    fnc(i,i)

cnt=0
for k,s in ans.items():
    cnt=cnt + len(set(s))
print(cnt)