from collections import deque

n=int(input())
tlist=[]
cond={}

for i in range(n):
    p=list(map(int,input().split()))
    tlist.append(p[0])
    cond[i]=p[2:]

#print(tlist)
#print(cond)

total=0
train=deque([n])
while len(train)>0:
    a1=train.pop()-1
    total+=tlist[a1]
    train.extend(cond[a1])
    tlist[a1]=0
    cond[a1]=[]

print(total)