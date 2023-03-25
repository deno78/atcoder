nlist=list(input())
nlist.sort(reverse=True)
n=len(nlist)
ans=0
for i in range(2 ** n):
    s1=[]
    s2=[]
    for j in range(n):
        if((i>>j) &1):
            s1.append(nlist[j])
        else:
            s2.append(nlist[j])
    if len(s1)>0 and len(s2)>0:
        n1=int("".join(s1))
        n2=int("".join(s2))
        ans=max(n1*n2,ans)
print(ans)