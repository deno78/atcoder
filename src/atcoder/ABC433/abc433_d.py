def concat(x,y):
    return [int(str(x)+str(y)),int(str(y)+str(x))]

n,m=map(int,input().split())
alist=list(map(int,input().split()))
adict={}
for a in alist:
    if a not in adict.keys():
        adict[a]=0
    adict[a]+=1

akeys=list(adict.keys())
ans=0
chk=set()
for i in range(len(akeys)):
    for j in range(i,len(akeys)):
        a1=akeys[i]
        a2=akeys[j]
        c1=adict[a1]
        c2=adict[a2]
        xy=concat(a1,a2)
        if i==j:
            z=xy[0]
            if z%m==0:
                ans+=(c1*c2)
        else:
            for z in xy:
    #            print(i,j,z,z%m)
                if z%m==0:
                    ans+=(c1*c2)

print(ans)
