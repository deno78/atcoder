xy = input('').split()
x = int(xy[0])
y = int(xy[1])

if  max(x,y) - min(x,y) < 3:
    print('Yes')
else:
    print('No')