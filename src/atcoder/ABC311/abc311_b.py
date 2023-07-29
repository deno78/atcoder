n,d=map(int,input().split())
slist=[]
for i in range(n):
    slist.append(list(input()))

ans=0
wk=0
for i in range(d):
    ok=True
    for j in range(n):
        if slist[j][i]!="o":
            ok=False
            ans=max(ans,wk)
            wk=0
            break
    if ok:
        wk+=1

ans=max(ans,wk)
print(ans)
        
