n  = int(input(''))

cnt=0
result="No"
for i in range(n):
    d12 = input('').split()
    d1 = d12[0]
    d2 = d12[1]
    if d1 == d2:
        cnt+=1
        if cnt ==3:
            result = "Yes"
    else:
        cnt=0


print(result)
