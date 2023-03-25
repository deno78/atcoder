s=[]
s.append(input())
s.append(input())
s.append(input())
s.append(input())

s2=['H','2B','3B','HR']

ok=True
for a in s2:
    if s.count(a)!=1:
        ok=False

if ok:
    print('Yes')
else:
    print('No')

