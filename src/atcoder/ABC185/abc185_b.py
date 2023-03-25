nmt = input('').split()
n = int(nmt[0])
m = int(nmt[1])
t = int(nmt[2])
f=n

c = 0
for i in range(m):
    ab = input('').split()
    a = int(ab[0])
    b = int(ab[1])
    n -= (a-c)
#    print("[{}] {}-{} ->{}".format(c,a,b,n))
    if n <=0:
        print('No')
        exit(0)
    n += (b-a)
    n = min(f,n)
    c=b

#print("{}-{} ->{}".format(c,t,n))
n -= (t-c)
if n <=0:
    print('No')
else:
    print('Yes')