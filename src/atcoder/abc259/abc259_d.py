# TODO edit the code

# param
n = int(input())
sx,sy,tx,ty=map(int,input().split())
si=-1
ti=-1

xyr = []
for i in range(n):
    x,y,r =map(int,input().split())
    xyr.append([x,y,r])
    if (x-sx)**2 + (y-sy)**2==r**2:
        si=i
    if (x-tx)**2 + (y-ty)**2==r**2:
        ti=i

# solve
dp=[]
dp.append(xyr[si])
xt,yt,rt=xyr[ti]

cnt=len(xyr)
while len(dp)>0:
    x1,y1,r1=dp.pop()
    xyr2=[]
    for x2,y2,r2 in xyr:
#        print("{} {} {} / {} {} {}".format(x1,y1,r1,x2,y2,r2))
        if ((x1-x2)**2 + (y1-y2)**2 <= (r1+r2)**2):
            if x1 == x2 and y1 == y2 and r1 != r2:
                xyr2.append([x2,y2,r2])
            elif xt==x2 and yt==y2 and r2==rt:
                print("Yes")
                exit()
            else:
                dp.append([x2,y2,r2])
        else:
            xyr2.append([x2,y2,r2])
    if cnt == len(xyr2):
        break
    xyr=xyr2

print("No")
