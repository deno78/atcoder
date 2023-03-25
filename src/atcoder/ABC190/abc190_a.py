abc = input('').split()
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

if c==0:
    if a>b:
        print('Takahashi ')
    else:
        print('Aoki')
else:
    if a>=b:
        print('Takahashi ')
    else:
        print('Aoki')
