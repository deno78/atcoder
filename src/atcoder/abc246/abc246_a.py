# TODO edit the code

# param
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

# solve
xs=[x1,x2,x3]
ys=[y1,y2,y3]

x=-1
y=-1
for s in xs:
    if xs.count(s)==1:
        x=s
for s in ys:
    if ys.count(s)==1:
        y=s

# answer
print("{} {}".format(x,y))