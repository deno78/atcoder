abxy=list(map(int,input().split()))
a=abxy[0]
b=abxy[1]
x=abxy[2]
y=abxy[3]

diff=b-a
if diff<0:
    diff=abs(diff)-1

kaidan=x+diff*y
rouka=(diff*2+1)+x

print(min(kaidan,rouka))