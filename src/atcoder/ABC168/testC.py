import math
abhm = input('')
a=int(abhm.split(' ')[0])
b=int(abhm.split(' ')[1])
h=int(abhm.split(' ')[2])
m=int(abhm.split(' ')[3])

hx=360/12*h + 360/(12*60)*m
mx=360/60*m

#print("hx:{}/{} mx:{}/{}".format(h,hx,m,mx))

angle = abs(hx-mx)
if angle > 180:
    angle = abs(angle-360)

c2 = pow(a,2) + pow(b,2) - 2*a*b*math.cos(math.radians(angle))
#print("a:{} b:{} c**2:{} angle:{}->cos:{}".format(a,b,c2,angle,math.cos(math.radians(angle))))

print(math.sqrt(abs(c2)))
