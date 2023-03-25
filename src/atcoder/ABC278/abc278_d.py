n=int(input())
alist=list(map(int,input().split()))

q=int(input())

adict={}
for i in range(1,n+1):
    adict[i]=alist[i-1]

a=0
for i in range(q):
    l=input().split()
    t=l[0]
    i=int(l[1])
    if t=="1":
        a=i
        adict={}
    elif t=="2":
        x=int(l[2])
        if i in adict.keys():
            adict[i]+=x
        else:
            adict[i]=x
    elif t=="3":
        if i in adict.keys():
            print(a+adict[i])
        else:
            print(a)

#    print("all:{} a:{} b:{}".format(a,alist,blist))

