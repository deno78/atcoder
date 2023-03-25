ssgg  = input('').split()
sx=int(ssgg[0])
sy=int(ssgg[1])
gx=int(ssgg[2])
gy=int(ssgg[3])


d=(-1*gy-sy)/(gx-sx)
h = sy - (d*sx)

a =-1* h/d

print(a)
