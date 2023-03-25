h=int(input())

mlist=[h]*1

cnt=0
while len(mlist)>0:
    x=mlist.pop(0)
    if x!=1:
        mlist.append(x//2)
        mlist.append(x//2)
    cnt+=1

print(cnt)