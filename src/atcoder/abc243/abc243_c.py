# TODO edit the code

# param
n = int(input())
xy=[]
for i in range(n):
    xy.append(list(map(int,input().split())))
s=input()

ydic={}
for i in range(n):
    x,y=xy[i]
    c=s[i]
    if y not in ydic.keys():
        ydic[y]={}
    if c not in ydic[y].keys():
        ydic[y][c]=[]
    ydic[y][c].append(x)
# solve
for y,xcs in ydic.items():
    if "L" in xcs.keys() and "R" in xcs.keys():
        xl=max(xcs["L"])
        xr=min(xcs["R"])
#        print("[{}] L:{} R:{}".format(y,xl,xr))
        if xl>=xr:
            print("Yes")
            exit()
print("No")