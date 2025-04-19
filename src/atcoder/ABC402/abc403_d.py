n, m = map(int, input().split())
ablist = []
abdict={}
for i in range(m):
    a,b=map(int,input().split())
    x=a+b
    if x not in abdict.keys():
        abdict[x]=0
    abdict[x]+=1

l=len(abdict.keys())
klist=list(abdict.keys())
ans = m*(m-1)//2
for i in range(l):
    k=klist[i]
    x=abdict[k]
    ans-=(x*(x-1)//2)
    if k+n in abdict.keys():
        x1=abdict[k]
        x2=abdict[k+n]
        ans-=(x1*x2)

print(ans)