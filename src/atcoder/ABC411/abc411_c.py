n,q=map(int,input().split())
alist=list(map(int,input().split()))

wk=[0]*n
ans=0

for a in alist:
    a-=1
    if n==1:
        if wk[a]==0:
            ans+=1
        else:
            ans-=1
    else:
        if a==0:
            t2=wk[a]
            t3=wk[a+1]
            if t2==0 and t3==0:
                ans+=1
            elif t2==1 and t3==0:
                ans-=1
        elif a==n-1:
            t1=wk[a-1]
            t2=wk[a]
            if t1==0 and t2==0:
                ans+=1
            elif t1==0 and t2==1:
                ans-=1
        else:
            t1=wk[a-1]
            t2=wk[a]
            t3=wk[a+1]
            if t1==0 and t2==0 and t3==0:
                ans+=1
            elif t1==0 and t2==1 and t3==0:
                ans-=1
            elif t1==1 and t2==0 and t3==1:
                ans-=1
            elif t1==1 and t2==1 and t3==1:
                ans+=1
    wk[a]=(wk[a]+1)%2
    print(ans)