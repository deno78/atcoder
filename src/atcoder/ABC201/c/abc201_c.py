s=input()

x1=[]
x2=[]
x3=[]
for i in len(s):
    if s[i]=='o':
        x1.append(str(i))
    elif s[i]=='x':
        x2.append(str(i))
    elif s[i]=='?':
        x3.append(str(i))

cnt=0
for i in range(10000):
    flgs=[]
    for c in str(i):
        if c in x2:
            continue
        if c in x1 and c not in flgs:
            flgs.append(c)
        if c in x3:
