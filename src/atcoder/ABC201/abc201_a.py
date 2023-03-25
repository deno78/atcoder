a=list(map(int,input().split()))
a=sorted(a)
a1=a[0]
a2=a[1]

a3=a[2]

if abs(a1-a2) == abs(a2-a3):
    print('Yes')
else:
    print('No')