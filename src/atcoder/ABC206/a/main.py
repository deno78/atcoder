import math
n=int(input())

x=math.floor(1.08*n)
#print(x)
if x < 206:
    print('Yay!')
elif x == 206:
    print('so-so')
else:
    print(':(')