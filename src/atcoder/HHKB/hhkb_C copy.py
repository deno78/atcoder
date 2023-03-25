n = int(input(''))
plist = list(map(int,input('').split()))

lastmin = 0
for i in range(1,n+1):
    p2 = plist[0:i]
    if min(p2) == 0:
    if min(p2) == 0:
        p2.sort()
        for j in range(lastmin,i):
            if j not in p2:
                print(j)
                lastmin = j
                break
    else:
        print("0")

