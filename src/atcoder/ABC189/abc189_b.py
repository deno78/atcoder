nx = input('').split()
n = int(nx[0])
x = int(nx[1])

a = 0
for i in range(n):
    vp = list(map(int,input('').split()))
    v=vp[0]
    p=vp[1]
    a+=v*p
    if a > x*100:
        print(i+1)
        exit(0)

print("-1")
exit(0)