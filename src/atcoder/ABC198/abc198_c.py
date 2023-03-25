import math
rxy=list(map(int,input().split()))
r=rxy[0]
x=rxy[1]
y=rxy[2]

r2= math.sqrt(x**2+y**2)
m=int(math.ceil(r2/r))
if m==1 and r2!=r:
    print(m+1)
else:
    print(m)
