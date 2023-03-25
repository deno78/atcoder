nmx = input('')
n=int(nmx.split(' ')[0])
m=int(nmx.split(' ')[1])
x=int(nmx.split(' ')[2])

map = {}
for i in range(n):
    cas = input('')
    c = int(cas.split(' ')[0])
    alist=[]
    for j in range(m):
        alist.append(int(cas.split(' ')[j]))
    map[c]=alist

mx=-1
for i in range(2**n):
    idx=i
    money=0
    skilllist=[0]*m
    buylist=[False]*n
    for j in range(n):        
        print("{} / {} = {}".format(i,2**j,i % (2**j)))
        if i % (2**j)==0:
            buylist[j]==True
            for k in range(m):
                skilllist[k]+=map[c][k]
    print(buylist)
    ok=True
    for j in range(m):
        if skilllist[j]<x:
            ok = False
            break
    if ok==True:
        if mx == -1:
            mx=money
        elif money < mx:
            mx=money


print(mx)

