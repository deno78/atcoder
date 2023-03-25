nsd = input('').split()
n = int(nsd[0])
s = int(nsd[1])
d = int(nsd[2])

ans=0
for i in range(n):
    xy = input('').split()
    x = int(xy[0])
    y = int(xy[1])
    if x < s and y > d:
        ans=1

if ans==1:
    print('Yes')
else:
    print('No')
