ak=input().split()
a=int(ak[0])
k=int(ak[1])

w=2*10**12

if k==0:
    print(w-a)
    exit()

t=a
d=0
while t<w:
    d+=1
    s=k*t+1
    t+=s
print(d)
