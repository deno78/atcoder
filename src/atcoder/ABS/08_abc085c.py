ny = input('')
n = int(ny.split(' ')[0])
y = int(ny.split(' ')[1])

ok = False
for i in range(n+1,0,-1):
    for j in range(n+1-i,0,-1):
        k = n-i-j
        if (i*10000 + j*5000 + k*1000)==y:
            ok = True
            print("{} {} {}".format(i,j,k))
            break
    if ok:
        break

if not ok:
    print("-1 -1 -1")

