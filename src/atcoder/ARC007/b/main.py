nm=input().split()
n=int(nm[0])
m=int(nm[1])

dlist=[]
for i in range(m):
    dlist.append(int(input()))

# CDとケースの連想配列
cmap={}
for i in range(n+1):
    cmap[i]=i

for d1 in dlist:
    p1=cmap[d1] # 聞いた曲のケース位置
    p2=0 # 聞いた曲の移動先
    for k,v in cmap.items():
        if v==0:
            d2=k
            break
    cmap[d1]=p2
    cmap[d2]=p1

#    print(cmap.values())

for i in range(1,n+1):
    for  k,v in cmap.items():
        if v==i:
            print(k)
