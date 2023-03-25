n = int(input(''))
alist = list(map(int,input('').split()))

n2=2**n

m=int(n2/2)

alist1=alist[:m]
alist2=alist[m:]

a1=max(alist1)
a2=max(alist2)

print(alist.index(min(a1,a2))+1)
