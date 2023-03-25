import math

def f(x,y,v):
    if y < v:
        return 0
    s = (x-1)//v+1
    e = y//v
    print("[{}-{}]:{} -> [{}-{}]".format(x,y,v,s,e))
    return e - s+1

abcd = input('').split()
a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

cd = (c*d) // math.gcd(c,d)

cx = f(a,b,c)
dx = f(a,b,d)
cdx = f(a,b,cd)

print("c:{} d:{} c&d:{}".format(cx,dx,cdx))

print(b - a - cx - dx + cdx + 1)
