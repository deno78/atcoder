a,b,c,d=map(int,input().split())

x=0
y=0
dy=None
while True:
    x+=1
    y=a+b*x - c*x*d
#    print("[{}] {} - {} = {}".format(x,a+b*x,c*x*d,y))
    if y<=0:
        print(x)
        exit()
    if dy!= None and dy<=y:
        print(-1)
        exit()
    dy=y