n=int(input())
alist=list(map(int,input().split()))

ans=0
for l in range(n):
    for r in range(l,n):
        all=sum(alist[l:r+1])
        ok=True
        for i in range(l,r+1):
            a=alist[i]
            if all%a==0:
                ok=False
                break
#        print(l,r,alist[l],alist[r],all)
        if ok:
            ans+=1

print(ans)
