import math

nm=input().split()
n=int(nm[0])
m=int(nm[1])

mlist=[0]*n

for i in range(m):
    ab=input().split()
    a=int(ab[0])-1
    b=int(ab[1])-1
    mlist[a]=mlist[a]+1
    mlist[b]=mlist[b]+1

cnt1=0
cnt2=0
cnt0=0
for x in mlist:
    if x==3:
        print(0)
        exit()
    elif x==0:
        cnt0=cnt0+1
    elif x==1:
        cnt1=cnt1+1
    elif x==2:
        cnt2=cnt2+1

cnt=1
if cnt0>0:
    cnt=cnt*(3**cnt0)
if cnt1>0:
    cnt=cnt*(math.factorial(cnt1)*2)
if cnt2>0:
    cnt=cnt*(math.factorial(cnt2))

print(cnt)

