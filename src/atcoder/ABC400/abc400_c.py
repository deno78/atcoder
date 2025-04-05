import bisect

n=int(input())

alist=[]
bset=set([])
a=1
for i in range(n):
    a*=2
    if a>n:
        break
    alist.append(a)
for i in range(n):
    b=(i*2+1)**2
    if b>n:
        break
    bset.add(b)
ans=0

for b in bset:
    x2=n//b
    idx=bisect.bisect(alist,x2)
    ans+=idx
#    print("[{}] {} x {}".format(i,b,idx))

print(ans)