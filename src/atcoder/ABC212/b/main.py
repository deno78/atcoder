x=list(map(int,list(input())))

if len(set(x))==1:
    print('Weak')
    exit()

ok=True
x2=x[0]
for i in range(1,4):
    if x[i] != (x2+1)%10:
        ok=False
        break
    x2=x[i]%10
    
if ok:
    print('Weak')
else:
    print('Strong')