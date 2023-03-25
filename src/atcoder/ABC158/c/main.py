import math
a,b=map(int,input().split())

p=a*100//8

#print("p:{} a2:{} b2:{}".format(p,a2,b2))

for i in range(100):
    a2=math.floor(p*0.08)
    b2=math.floor(p*0.10)
    if a==a2 and b==b2:
        print(int(p))
        exit()
    p+=1
print(-1)