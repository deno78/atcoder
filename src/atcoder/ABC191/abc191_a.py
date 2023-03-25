vtsd = input('').split()
v=int(vtsd[0])
t=int(vtsd[1])
s=int(vtsd[2])
d=int(vtsd[3])

#print("d:{} vt:{} vs:{}".format(d,v*t,v*s))
if d >= v*t and d <= v*s:
    print('No')
else:
    print('Yes')
