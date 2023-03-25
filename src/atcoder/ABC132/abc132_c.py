n=int(input(''))
dlist = list(map(int,input('').split()))

dlist.sort()
#print(dlist)
n1 = dlist[int(n/2)-1]
n2 = dlist[int(n/2)]

#print("{}-{}".format(n1,n2))
print(n2-n1)
