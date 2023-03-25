n = int(input(''))
alist = list(map(int,input('').split()))

cnt=0

ok = True
while ok:
    for i in range(len(alist)):
        a = alist[i]
        if a%2 == 0:
            alist[i] = a/2
        else:
            ok = False
    if ok:
        cnt+=1

print(cnt)