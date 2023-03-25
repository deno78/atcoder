import bisect

# TODO edit the code
def primeNumberCreate(maxNumber):
    max = int(maxNumber**(1/2))
    seachList = [i for i in range(2,maxNumber+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

# param
n = int(input())

m=int(n**(1/3))+1

# solve
plist= primeNumberCreate(m)
l=len(plist)
ans=0
for i in range(1,l):
    q=plist[i]
    q2=q**3
    n2=n//q2
    i2=bisect.bisect(plist,n2,hi=i)
#    print("q:{}-> q2:{} n2:{} i={}".format(q,q2,n2,i2))
    ans+=min(i,i2)

# answer
print(ans)
