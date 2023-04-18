import math
x=int(input())

x2=0
while True:
    x2+=1
    if 2**x2>x:
        break
x2+=2

x1=int(math.sqrt(x))+1
ans=0
for i in range(1,x1):
    for j in range(2,x2):
        y=i**j
        if y<=x:
            ans=max(ans,y)

print(ans)
