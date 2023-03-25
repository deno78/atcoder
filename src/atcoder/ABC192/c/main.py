def g1(x):
    tmp=list(str(x))
    tmp.sort(reverse=True)
    return int("".join(tmp))

def g2(x):
    tmp=list(str(x))
    tmp.sort()
    return int("".join(tmp))

nk=input().split()
n=int(nk[0])
k=int(nk[1])

a=n
for i in range(k):
    a=g1(a)-g2(a)

print(a)