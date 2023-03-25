nk = input('')
n = int(nk.split()[0])
k = int(nk.split()[1])

alist = list(map(int,input('').split()))

for i in range(1,n-k+1):
    removed = alist[i-1]
    inserted = alist[i+k-1]
    if inserted > removed:
        print('Yes')
    else:
        print('No')
