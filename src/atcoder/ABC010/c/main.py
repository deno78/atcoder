
txa,tya,txb,tyb,t,v=map(int,input().split())

n=int(input())
xylist=[]
for i in range(n):
    xylist.append(list(map(int,input().split())))

l1=(t*v)
ok=True
for xy in xylist:
    x=xy[0]
    y=xy[1]
    l2=((txa-x)**2 + (tya-y)**2)**0.5 +((txb-x)**2 + (tyb-y)**2)**0.5
#    print("L1:{}/L2:{}".format(l1,l2))
    if l1 >= l2:
        ok=False

if ok:
    print("NO")
else:
    print("YES")