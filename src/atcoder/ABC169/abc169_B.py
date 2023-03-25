n = int(input(''))
alist = list(map(int,input('').split(' ')))

if 0 in alist:
    result=0
else:
    result=1
    for a in alist:
        result*= a
        if result > 10**18:
            result = -1
            break

print(result)