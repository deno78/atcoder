def checkleft(t1,t2):
    if t1 in [1,2] and t2 in [1,2]:
        return True
    elif t1 in [3,4] and t2 in [3,4]:
        return True
    else:
        return False

def checkright(t1,t2):
    if t1 in [1,3] and t2 in [1,3]:
        return True
    if t1 in [2,4] and t2 in [2,4]:
        return True
    else:
        return False

def checkleftright(t1,t2):
    if t1 in [1,3] and t2 in [1,2]:
        return True
    else:
        return False

n=int(input())
nlist=[]
for i in range(n):
    nlist.append(list(map(int,input().split())))

cnt=0
for i in range(len(nlist)-1):
    for j in range(i+1,len(nlist)):
        t1,l1,r1=map(int,nlist[i])
        t2,l2,r2=map(int,nlist[j])
        c1=checkleft(t1,t2)
        c2=checkright(t1,t2)
        c3=checkleftright(t1,t2)
        c4=checkleftright(t2,t1)
#        print("{}/{}/{} - {}/{}/{} {}/{}/{}/{}".format(t1,l1,r1,t2,l2,r2,c1,c2,c3,c4))
        if l1<r2 and l2<r1:
            cnt+=1
        elif l1<r2 and l2==r1 and c3:
            cnt+=1
        elif l1==r2 and l2<r1 and c4:
            cnt+=1

print(cnt)