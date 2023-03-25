# TODO edit this code

# param
n,p,q,r = map(int,input().split())
alist=list(map(int,input().split()))

blist=[]
x=0
blist.append(0)
for a in alist:
    x+=a
    blist.append(x)

# solve
x=0
y=1
z=2
w=3
while x<len(blist) and y<len(blist) and z<len(blist)and w<len(blist):
    a=blist[y]-blist[x]
    b=blist[z]-blist[y]
    c=blist[w]-blist[z]
    if a==p and b==q and c==r:
#        print("{} {} {} {}".format(x,y,z,w))
        print('Yes')
        exit()
    if c<r:
        w+=1
    elif c>r:
        z+=1
    elif b<q:
        z+=1
    elif b>q:
        y+=1
    elif a<p:
        y+=1
    elif a>p:
        x+=1
#    print("{} {} {} {}".format(x,y,z,w))

# answer
print("No")