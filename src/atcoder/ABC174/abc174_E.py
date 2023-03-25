import math
nk = input('').split()
n = int(nk[0])
k = int(nk[1])
alist = list(map(int,input('').split()))

alist.sort()
avg = sum(alist)/(n+k)

print(alist)
print(avg)

for i in range(k):
    a = alist.pop(-1)
    if a>avg*3:
        a1=avg
        a2=a-avg
    else:
        a1=a/2
        a2=a/2
    alist.append(a1)
    alist.append(a2)
    print("{} ->{}/{}".format(a,a1,a2))
    alist.sort()

alist.sort()
print(alist)
print(math.ceil(alist[-1]))