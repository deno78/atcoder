import math
x = int(input(''))

m=100
y=0
while m < x:
    y+=1
    m=math.floor(m*1.01)

print(y)
