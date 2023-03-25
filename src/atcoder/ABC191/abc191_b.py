nx = input('').split()
n = int(nx[0])
x = int(nx[1])

alist = list(map(int,input('').split()))

blist = []
for a in alist:
    if a != x:
        blist.append(str(a))

print(" ".join(blist))