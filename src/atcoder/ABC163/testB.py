nm = input('')
n = int(nm.split(' ')[0])
m = int(nm.split(' ')[1])

alist = input('').split(' ')

d=0
for a in alist:
    d+=int(a)

if n >= d:
    print(n-d)
else:
    print('-1')
