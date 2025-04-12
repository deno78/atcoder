n=int(input())
slist=[]
for i in range(n):
    slist.append(input())

ans=0
islogin=False

for i in range(n):
    s=slist[i]
    if s=="login":
        islogin=True
    elif s=="logout":
        islogin=False
    elif s=="private":
        if not islogin:
            ans+=1

print(ans)