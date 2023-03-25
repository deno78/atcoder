import math
# TODO edit the code

# param
a,b,d = map(int,input().split())
if a == 0 and b == 0:
    print("0 0")
    exit()

c2 = (a**2 + b**2)**0.5
if a==0 and b >0:
    d1 = 90
elif a==0 and b < 0:
    d1 = -90
else:
    d1 = math.degrees( math.atan2(b,a))
d2=(d+d1)%360
# solve
x = math.cos(math.radians(d2))
y = math.sin(math.radians(d2))

# answer
print("{} {}".format(x*c2,y*c2))
