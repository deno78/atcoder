xy = input('')
x = int(xy.split(' ')[0])
y = int(xy.split(' ')[1])

result = False
for a in range(x+1):
    b = x - a
    print("a:{} b:{} =>{}".format(a,b,a*2+4*b))
    if (a*2 + 4*b) == y:
        result = True

if result:
    print('Yes')
else:
    print('No')