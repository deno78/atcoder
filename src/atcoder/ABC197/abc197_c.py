n = int(input())
a = list(map(int,input().split()))
m=2**30

for i in range(2**(n-1)):
    o=a[0]
    x=[]
    for j in range(n-1):
        if ((i >>j)&1):
#            print("or:{} | {}".format(o,a[j+1]))
            o = o | a[j+1]
        else:
            x.append(o)
            o = a[j+1]
    x.append(o)
    ans=0
    for x2 in x:
        ans=ans^x2
    m=min(ans,m)
print(m)
