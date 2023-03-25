# TODO edit this code

# param
h,w=map(int,input().split())

g=[]
for i in range(h):
    g.append(list(input()))

hist={}
hist[0]=[0]
x=0
y=0
# solve
while True:
    if g[y][x] == "U":
        if y==0:
            print("{} {}".format(y+1,x+1))
            exit()
        else:
            y-=1
    elif g[y][x] == "D":
        if y==h-1:
            print("{} {}".format(y+1,x+1))
            exit()
        else:
            y+=1
    elif g[y][x] == "R":
        if x==w-1:
            print("{} {}".format(y+1,x+1))
            exit()
        else:
            x+=1
    elif g[y][x] == "L":
        if x==0:
            print("{} {}".format(y+1,x+1))
            exit()
        else:
            x-=1
    if x in hist.keys() and y in hist[x]:
        print("-1")
        exit()
    else:
        if x not in hist.keys():
            hist[x]=[]
        hist[x].append(y)

