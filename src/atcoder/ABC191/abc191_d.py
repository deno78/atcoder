import math

xyr = input('').split()
x=int(float(xyr[0])*10000)
y=int(float(xyr[1])*10000)
r=int(float(xyr[2])*10000)

cnt=0
for i in range(x-r-1,x+r+2):
    if i >= (x-r) and i <= (x+r):
        h2 = r**2 - abs(x-i)**2
        cnt+=int(math.sqrt(h2)/10000/10000)

print(cnt)