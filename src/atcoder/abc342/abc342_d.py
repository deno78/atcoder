# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
alist = list(map(int, input().split()))
adict={}
for i in range(n):
    a=alist[i]
    if a not in adict.keys():
        adict[a]=0
    adict[a]+=1

# solve
sq=[]
mx=max(alist)**2
i=0
while i**2<=mx:
    sq.append(i**2)
    i+=1
ans=0
alist2=list(adict.keys())
for i in range(len(alist2)-1):
    for j in range(i+1,len(alist2)):
        a1=alist2[i]
        a2=alist2[j]
        if a1*a2 in sq:
            ans+=(adict[a1]*adict[a2])
for i in range(len(alist2)):
    a1=alist2[i]
    if a1**2 in sq:
        ans+=(adict[a1] * (adict[a1]-1))//2

# answer
print("{}".format(ans))
