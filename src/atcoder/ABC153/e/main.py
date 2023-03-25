h,n=map(int,input().split())
ablist=[]
m=0
mi=-1
for i in range(n):
    a,b=map(int,input().split())
    ablist.append([a,b])
    if m<(a/b):
        m=a/b
        mi=i
print(ablist)
print("[{}]:{}".format(mi,i))

a1=ablist[mi][0]
b1=ablist[mi][1]
x=h//a1
y=h%a1
c1=x*b1

print("{}/{} * {} rest:{}".format(a1,b1,x,y))
if y==0:
    print(c1)
else:
    c2=b1
    for a,b in ablist:
        x2=y//a
        if y%a==0:
            c=x2*b
        else:
            c=(x2+1)*b
        c2=min(c2,c)
        print("rest={} {}/{} ->{}".format(y,a,b,c2))
    print(c1+c2)
