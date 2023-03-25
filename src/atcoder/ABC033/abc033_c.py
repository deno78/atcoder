s=input()

ans=0
clist=s.split("+")
for c in clist:
    if "0" not in c:
        ans+=1

print(ans)
    