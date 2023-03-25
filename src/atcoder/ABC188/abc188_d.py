nc = input('').split()
n = int(nc[0])
c = int(nc[1])

aclist=[]
bclist=[]
days=[]
for i in range(n):
    abc = list(map(int,input('').split()))
    aclist.append([abc[0],abc[2]])
    bclist.append([abc[1],abc[2]])
    if abc[0] not in days:
        days.append(abc[0])
    if abc[1] not in days:
        days.append(abc[1])

aclist.sort()
bclist.sort()

price=0
total=0
for i in range(len(days)):
    day=days[i]
    next_day=max(days)
    if i!=len(days)-1:
        days[i+1]-1
    for ac in aclist:
        if ac[0] == day:
            price+=ac[1]
    for bc in bclist:
        if bc[0] == day:
            price-=bc[1]
    print(price)
