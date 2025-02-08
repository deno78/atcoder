# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
klist=[]
akdict={}
for i in range(n):
    ak=list(map(int, input().split()))
    k=ak[0]
    klist.append(k)
    alist=ak[1:]
    adict={}
    for j in range(k):
        a=alist[j]
        if a not in adict.keys():
            adict[a]=0
        adict[a]+=1
    akdict[i]=[k,adict]

# solve
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        k1=akdict[i][0]
        k2=akdict[j][0]
        adict1=akdict[i][1]
        adict2=akdict[j][1]
        v=0
        for a in adict1.keys():
            if a in adict2.keys():
                v1=adict1[a]
                v2=adict2[a]
                v+=v1/k1*v2/k2
#                print("[{}/{}] {}={},{}".format(i,j,a,v1,v2))
        ans=max(ans,v)
#        print("[{}/{}]{}".format(i,j,v))

# answer
print(ans)