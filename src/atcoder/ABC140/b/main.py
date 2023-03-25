n=int(input())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
clist=list(map(int,input().split()))

m=0 # 満足度
d=float('INF') # 1個前の状態
for i in range(n):
    # index=seq-1
    a=alist[i] - 1
    b=blist[a]
    m+=b
#    print("a:{} b:{} d:{}".format(a,b,d))
    if d+1==a:
        c=clist[a-1]
        m+=c
    d=a
print(m)

