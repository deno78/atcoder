def calc(n,alist):
    ret=set()
    d={}
    for i in range(n):
        d[i]=[]
    for i in range(n*2):
        a=alist[i]
        a-=1
        d[a].append(i)
    for i in range(n):
        i2=i*2
        j=i2+1
        a1=alist[i2]
        a2=alist[j]
        a1-=1
        a2-=1
        if abs(d[a1][0]-d[a2][0])==1 and abs(d[a1][1]-d[a2][1])==1:
            r=[str(a1),str(a2)]
            r.sort()
            ret.add("-".join(r))
#    print(ret)
    return len(ret)

t=int(input())
nalist=[]
for i in range(t):
    n=int(input())
    alist=list(map(int,input().split()))
    nalist.append([n,alist])

for na in nalist:
    n=na[0]
    alist=na[1]
    ans=calc(n,alist)
    print(ans)