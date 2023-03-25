abc=list(map(int,input().split()))

a=abc[0]
b=abc[1]
c=abc[2]

c2=c%2+2

a2=a**c2
b2=b**c2

if a2 < b2:
    print('<')
elif a2 > b2:
    print('>')
elif a2==b2:
    print('=')
