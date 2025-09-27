n,q=map(int,input().split())
alist=list(map(int,input().split()))
query=[]
for i in range(q):
    query.append(list(map(int,input().split())))

blist=[0]
w=0
for i in range(n):
    a=alist[i]
    w+=a
    blist.append(w)
for i in range(n):
    a=alist[i]
    w+=a
    blist.append(w)
p=0
n2=len(blist)
for qu in query:
    q1=qu[0]
    if q1==1:
        c=qu[1]
        p+=c
    elif q1==2:
        l=qu[1]-1
        r=qu[2]-1
        l+=p
        r+=p
        l%=n
        r%=n
        if r<l:
            r+=n
        ans=blist[r+1]-blist[l]
        print(ans)

