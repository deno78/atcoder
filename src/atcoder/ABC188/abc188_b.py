n = int(input(''))

alist = list(map(int,input('').split()))
blist = list(map(int,input('').split()))

s=0
for i in range(n):
    s+=alist[i]*blist[i]

if s==0:
    print('Yes')
else:
    print('No')