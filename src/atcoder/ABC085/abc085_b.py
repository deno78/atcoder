n = int(input(''))
dlist = []
for i in range(n):
    dlist.append(int(input('')))

dset = set(dlist)

print(len(dset))