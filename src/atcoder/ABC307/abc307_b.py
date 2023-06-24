n=int(input())
slist =[]
for i in range(n):
    slist.append(input())

chk=[]
for i in range(n):
    for j in range(n):
        if i!=j:
            chk.append(slist[i]+slist[j])

for c in chk:
    ok=True
    for i in range(len(c)//2):
        if c[i]!=c[-1*(i+1)]:
            ok=False
            break
    if ok:
        print('Yes')
        exit()
print('No')
