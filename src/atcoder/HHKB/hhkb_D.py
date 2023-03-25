import math
t = int(input(''))
for i in range(t):
    nab = input('').split()
    n = int(nab[0])
    a = int(nab[1])
    b = int(nab[2])
    x1 = (n-a+1)**2
    x2 = (n-b+1)**2
    if a > b:
        x3 = (a-b+1)**2 * x1
    else:
        x3 = (b-a+1)**2 * x2
    x = x1 * x2 - x3

    print("{} * {} - {} = {}".format(x1,x2,x3,x))
    print(x)

