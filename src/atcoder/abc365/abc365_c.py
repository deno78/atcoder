# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist = list(map(int, input().split()))

if sum(alist)<=m:
    print("infinite")
    exit()
aset=list(set(alist))
aset.sort()
key_size=len(aset)
adict={}
for i in range(n):
    a=alist[i]
    if a not in adict.keys():
        adict[a]=0
    adict[a]+=1

# solve
l=0
r=aset[-1]
ans=-1
while r-l>1:
    c=(l+r)//2
    x=0
    for i in range(key_size):
        a2=aset[i]
        num=adict[a2]
        x+=min(c,a2)*num
#    print("{}-{}-{}={}/{}".format(l,c,r,x,m))
    if x>m:
        r=c
    else:
        l=c
        ans=max(ans,c)
print(ans)