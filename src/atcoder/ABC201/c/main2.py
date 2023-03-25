s=list(input())

must=[]
not_must=[]
maybe=[]

for i in range(len(s)):
    c=s[i]
    if c=='o':
        must.append(str(i))
    elif c=='x':
        not_must.append(str(i))
    else:
        maybe.append(str(i))

cnt=0
for i in range(10000):
    s2=list(str(i).zfill(4))
    ok = True
    for c in must:
        if c not in s2:
            ok=False
    for c in not_must:
        if c in s2:
            ok=False
    if ok==True:
        cnt+=1
print(cnt)
