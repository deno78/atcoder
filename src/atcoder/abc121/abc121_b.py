n,m,c=map(int,input().split())

blist=list(map(int,input().split()))
alists=[]
for i  in range(n):
    alists.append(list(map(int,input().split())))

ans=0
for alist in alists:
    x=c
    for i in range(m):
        a=alist[i]
        b=blist[i]
        x+=a*b
    if x>0:
        ans+=1

print(ans)