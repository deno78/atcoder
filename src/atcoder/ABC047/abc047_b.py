w,h,n=map(int,input().split())
xya=[]
for i in range(n):
    x,y,a=map(int,input().split())
    xya.append([x,y,a])

x1=0
x2=w
y1=0
y2=h

for x,y,a in xya:
    if a==1:
        x1=max(x1,x)
    elif a==2:
        x2=min(x2,x)
    elif a==3:
        y1=max(y1,y)
    elif a==4:
        y2=min(y2,y)

# print("{}/{}/{}/{}".format(x1,x2,y1,y2))
print(max(x2-x1,0)*max(y2-y1,0))