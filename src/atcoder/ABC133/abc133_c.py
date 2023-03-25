lr = input('').split()
l = int(lr[0])
r = int(lr[1])

m = 2018
y=min(r,l+2019)

for i in range(l,y):
    for j in range(i+1,y+1):
        m1 = (i*j)%2019
        m = min(m1,m)
#        print("{} x {} = {} -> {}".format(i,j,m1,m))
print(m)
