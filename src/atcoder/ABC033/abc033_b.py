n=int(input())
slist=[]
plist=[]
for i in range(n):
    s,p=input().split()
    slist.append(s)
    plist.append(int(p))

a=sum(plist)
c="atcoder"
for i in range(n):
    if plist[i] >a//2:
        c=slist[i]

print(c)
