import math
# TODO edit the code

# param
a,b=map(int,input().split())

if a==0:
    x=0
    y=1
elif b==0:
    x=1
    y=0
else:
    t=math.atan(a/b)
    x=math.sin(t)
    y=math.cos(t)

# answer
print("{} {}".format(x,y))
