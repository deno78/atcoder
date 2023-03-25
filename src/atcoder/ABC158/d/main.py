s=list(input())

s1=[]
s2=[]

f=True
q=int(input())
for i in range(q):
    e=input().split()
    if e[0]=='1':
        f=not f
    elif e[0]=='2':
        if e[1]=='1':
            if f:
                s1.append(e[2])
            else:
                s2.append(e[2])
        elif e[1]=='2':
            if f:
                s2.append(e[2])
            else:
                s1.append(e[2])

if f:
    print("".join(reversed(s1)) + "".join(s) + "".join(s2))
else:
    print("".join(reversed(s2)) +  "".join(reversed(s)) + "".join(s1))
