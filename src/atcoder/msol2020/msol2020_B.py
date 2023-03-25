abc = input('')
a = int(abc.split()[0])
b = int(abc.split()[1])
c = int(abc.split()[2])
k = int(input(''))

result = False
for i in range(k):
    if a>=b:
        b*=2
    elif b>=c:
        c*=2
#    print('{}/{}/{}'.format(a,b,c))
    if a<b and b < c:
        result = True
        break

if result:
    print('Yes')
else:
    print('No')
        