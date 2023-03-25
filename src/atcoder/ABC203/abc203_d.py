import statistics

def getmed(i,j,k,alist):
    t=[]
    for a in range(i,i+k):
        t.extend(alist[a][j:j+k])
    ans=statistics.median_low(t)
    print("[{},{}] {} ->{}".format(i,j,t,ans))
    return ans


nk=input().split()
n=int(nk[0])
k=int(nk[1])

alist=[]
for i in range(n):
    alist.append(list(map(int,input().split())))

m=10**9
if n==k:
    t=[]
    for a in range(k):
        t.extend(alist[a])
    m=min(m,statistics.median_low(t))
    print(int(m))
    exit()
else:
    i=0
    j=0
    m=getmed(0,0,k,alist)
    while True:
        mx=10**9
        my=10**9
        if i+k+1<n:
            mx=getmed(i+1,j,k,alist)
        if j+k+1<n:
            my=getmed(i,j+1,k,alist)
        if mx>my:
            j+=1
            if my>m:
                print(m)
                exit()
            m=min(my,m)            
        else:
            i+=1
            if mx>m:
                print(m)
                exit()
            m=min(mx,m)
