n=int(input())
alist=list(map(int,input().split()))


blist=[]

alist13=sorted(alist[:3])
b1=alist13[2]
b2=alist13[1]
blist.append(alist13[0])

for i in range(3,n):
    a=alist[i]
    b=blist[i-3]
    if a>b1:
#        print("A:", a,b1,b2,b,blist)
        blist.append(b2)
        b2=b1
        b1=a
    elif a>b2:
#        print("B:", a,b1,b2,b,blist)
        blist.append(b2)
        b2=a
    else:
#        print("C:", a,b1,b2,b,blist)
        blist.append(max(b,a))

for b in blist:
    print(b)