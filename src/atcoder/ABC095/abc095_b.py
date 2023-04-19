n,x=map(int,input().split())
mlist=[]
for i in range(n):
    mlist.append(int(input()))

for i in range(n):
    x-=mlist[i]

a=x//min(mlist)

print(n+a)