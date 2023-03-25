n=int(input())
alist=list(map(int,input().split()))

adict={}
adict[1]=0

for i in range(1,n+1):
#    print("[{}] {}".format(i,adict))
    a=alist[i-1]
    adict[i*2]=adict[a]+1
    adict[i*2+1]=adict[a]+1
#    print(adict)

for i in range(1,2*n+2):
    print(adict[i])