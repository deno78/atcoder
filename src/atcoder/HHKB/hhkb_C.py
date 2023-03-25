n = int(input(''))
plist = list(map(int,input('').split()))

idx=0
alist = [0]*n

for i in range(n):
    p = plist[i]
    if p < n:
        alist[p]=1
#    print(alist)
    found = False
    for j in range(idx,n):
        if alist[j]==0:
            idx = j
            print(idx)
            found = True
            break
    if found == False:
        print(n)