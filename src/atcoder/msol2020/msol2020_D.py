n = int(input(''))
alist = list(map(int,input('').split()))
money=1000
stock=0

for d in range(n-1):
    if stock ==0:
        if alist[d+1] > alist[d]:
            # 明日上がるなら買い
            stock=int(money/alist[d])
            money-=stock*alist[d]
        else:
            # 明日下がる場合は何もしない
            pass
    else:
        if alist[d+1] > alist[d]:
            # 明日上がるなら全部売ってから買い
            money+=stock*alist[d]
            stock=int(money/alist[d])
            money-=stock*alist[d]
        else:
            # 明日下がる場合で株を持っていたら売り
            money+=stock*alist[d]
            stock=0

money+=stock*alist[n-1]
stock=0
print(money)