n,m=map(int,input().split())
alist=sorted(list(map(int,input().split())))
blist=sorted(list(map(int,input().split())))

if alist[0]>blist[-1]:
    print(abs(alist[0]-blist[-1]))
    exit()
if alist[-1]<blist[0]:
    print(abs(alist[-1]-blist[0]))
    exit()


ans=abs(alist[0]-blist[0])
i=0
j=0
while i<n and j<m:
#    print("[{},{}]=[{}/{}]".format(i,j,alist[i],blist[j]))
    a=alist[i]
    b=blist[j]
    ans=min(ans,abs(a-b))
    if a<b:
        if i<n:
            i+=1
    else:
        if j<m:
            j+=1

print(ans)
