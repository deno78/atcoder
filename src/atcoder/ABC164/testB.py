abcd = input('')
a = int(abcd.split(' ')[0])
b = int(abcd.split(' ')[1])
c = int(abcd.split(' ')[2])
d = int(abcd.split(' ')[3])
while True:
    c-=b
    if c <=0:
        break
    a-=d
    if a <=0:
        break

if a > 0:
    print('Yes')
else:
    print('No')
