k = int(input(''))
ab = input('')
a = int(ab.split(' ')[0])
b = int(ab.split(' ')[1])

ret=0
for i in range(a,b+1):
    if i % k == 0:
        ret=1

if ret==0:
    print('NG')
else:
    print('OK')
