

r1,c1=map(int,input().split())
r2,c2=map(int,input().split())

c=0
while d>0:
    if r1==r2 and abs(c1-c2)<3:
        c+=1
        break
    elif c1==c2 and abs(c1-c2)<3:
        c+=1
        break
    elif abs(r1-r2)<3 and abs(c1-c2)<3:
        c+=1
        break
    else:
        if r1>r2 and c1>c2: