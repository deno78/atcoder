n = int(input(''))
alist = list(map(int,input('').split()))
blist = list(map(int,input('').split()))

m=0
f=0
for i in range(n+1):
    a = alist[i]
    b = 0
    if i==n:
        b = 0
    else:
        b = blist[i]
    m+=min(a,b+f)
    f=max(0,min(b+f-a,b))
#    print("[{}] {}->{} [{}] =[{}]".format(i,a,b,f,m))

print(m)