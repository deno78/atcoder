import math
    

n = int(input(''))

mx=int(math.sqrt(n))+1

fmap = {}

for x in range(1,mx):
    for y in range(1,mx):
        for z in range(1,mx):
            ans = x**2 + y**2 + z**2 + x*y + y*z + x*z
            if ans not in fmap.keys():
                fmap[ans] = 0
            fmap[ans] += 1

for i in range(1,n+1):
    if i in fmap.keys():
        print(fmap[i])
    else:
        print(0)