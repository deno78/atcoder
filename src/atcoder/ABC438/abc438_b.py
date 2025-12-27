n,m=map(int,input().split())
s=input()
t=input()

ans=float('inf')
for i in range(n-m+1):
    wk=0
#    print("#",i,s,s[i:i+m],t)
    for j in range(m):
        c1=int(s[i+j])
        c2=int(t[j])
        if c1>c2:
            wk+=c1-c2
        elif c1==c2:
            wk+=0
        else:
            wk+=c1+10-c2
    ans=min(ans,wk)

print(ans)
        