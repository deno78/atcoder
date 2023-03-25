
nd = input('')
n = int(nd.split()[0])
d = int(nd.split()[1])

d1=d**2
cnt=0
for i in range(n):
    xy=input('')
    x = int(xy.split()[0])
    y = int(xy.split()[1])
    d2 = x**2+y**2
    if d1 >=d2:
        cnt+=1
print(cnt)
