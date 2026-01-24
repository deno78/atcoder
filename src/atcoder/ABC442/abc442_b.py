q=int(input())
active=False
vol=0
for i in range(q):
    a=int(input())
    if a==1:
        vol+=1
    elif a==2:
        vol=max(vol-1,0)
    elif a==3:
        active=not active
    if vol>=3 and active:
        print("Yes")
    else:
        print("No")


