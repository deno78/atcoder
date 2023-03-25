nm = input('').split()
n = int(nm[0])
m = int(nm[1])

ablist=[]
for i in range(m):
    ab = input('').split()
    a = int(ab[0])
    b = int(ab[1])
    ablist.append([a,b])

cdlist=[]
k = int(input(''))
for i in range(k):
    cd = input('').split()
    c = int(cd[0])
    d = int(cd[1])
    cdlist.append([c,d])

ans=0
for i in range(2 ** k):
    bag = []
    total = 0
    for j in range(k):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(cdlist[j][0])
        else:
            bag.append(cdlist[j][1])

#    print(bag)
    t=0
    for ab in ablist:
        if ab[0] in bag and ab[1] in bag:
            t+=1
    ans=max(ans,t)
print(ans)

