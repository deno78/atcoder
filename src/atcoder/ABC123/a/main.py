a=[]
for i in range(5):
    a.append(int(input()))
k=int(input())
ok=True
for a1 in a:
    for a2 in a:
        if abs(a1-a2)>k:
            ok=False
            break

if ok:
    print('Yay!')
else:
    print(':(') 
