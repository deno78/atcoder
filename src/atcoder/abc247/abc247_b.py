# TODO edit the code

# param
n = int(input())
slist=[]
tlist=[]
for i in range(n):
    s,t=input().split()
    slist.append(s)
    tlist.append(t)

# solve
ans=[]

for i in range(n):
    s=slist[i]
    t=tlist[i]
    if s in ans and t in ans:
        print("No")
        exit()
    if slist.count(s)>1 and tlist.count(t)>1:
        print("No")
        exit()
    if slist.count(s)==1 and ((tlist.count(s)==0 and s!=t) or (tlist.count(t)==1 and s==t)):
        ans.append(s)
    elif tlist.count(t)==1 and ((slist.count(t)==0 and s!=t) or (slist.count(t)==1 and s==t)):
        ans.append(t)
    else:
        print("No")
        exit()


print("Yes")
exit()