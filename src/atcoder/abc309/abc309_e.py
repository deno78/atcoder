# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
from collections import deque

# param
n,m = map(int, input().split())
plist=list(map(int,input().split()))
xy=[]
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    xy.append([x,y])
 
# solve

ptree={}
for i in range(n):
    ptree[i]=[]
for i in range(n-1):
    p=plist[i]
    p-=1
    ptree[p].append(i+1)

print(ptree)

ages=[0]*n
ages2={}
ages2[0]=[0]
wk=deque()
wk.append(0)
while len(wk)>0:
    w=wk.popleft()
    ages2[ages[w]+1]=[]
    for c in ptree[w]:
        ages[c]=ages[w]+1
        wk.append(c)
        ages2[ages[w]+1].append(c)

print(ages2)


# answer
