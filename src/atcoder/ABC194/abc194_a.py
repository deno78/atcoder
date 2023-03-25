ab = input().split()
a=int(ab[0])
b=int(ab[1])

if (a+b)>=15 and b >=8:
    print('1')
elif (a+b)>=10 and b >= 3:
    print('2')
elif (a+b) >=3:
    print('3')
else:
    print('4')