n = int(input(''))
alist = input('').split(' ')

h = {}
for i in range(1,n):
    a = int(alist[i-1])
    if not a in h.keys():
        h[a]=0
    h[a]+=1

for i in range(1,n+1):
    if i in h.keys():
        print(h[i])
    else:
        print(0)
