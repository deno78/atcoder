n=input()

c=0
for i in reversed(range(len(n))):
    if n[i]=='0':
        c=c+1
    else:
        break

for i in range(c):
    n='0' + n
i2=0
for i in reversed(range(len(n))):
    if n[i] != n[i2]:
        print('No')
        exit()
    i2=i2+1

print('Yes')