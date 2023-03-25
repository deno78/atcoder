# param

n = int(input())

lrdic={}
alist=[]
for i in range(n):
    lr=list(map(int,input().split()))
    l=lr[0]
    r=lr[1]
    if l not in lrdic.keys():
        lrdic[l]=0
    if r not in lrdic.keys():
        lrdic[r]=0
    lrdic[l]+=1
    lrdic[r]-=1
    alist.append(l)
    alist.append(r)

alist=list(set(alist))
alist.sort()
t1=0
t2=0
ans1=[]
ans2=[]
for a in alist:
    t2=t1+lrdic[a]
    if t1==0 and t2>0:
        ans1.append(a)
    elif t1>0 and t2==0:
        ans2.append(a)
    t1=t2

#print(ans1)
#print(ans2)
for i in range(len(ans1)):
    print("{} {}".format(ans1[i],ans2[i]))