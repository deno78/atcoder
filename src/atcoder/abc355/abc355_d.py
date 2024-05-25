# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
klist=[]
ldict={}
rdict={}
for i in range(n):
    l,r = map(int, input().split())
    if l not in ldict.keys():
        ldict[l]=0
    ldict[l]+=1
    if r not in rdict.keys():
        rdict[r]=0
    rdict[r]+=1    
    klist.append(l)
    klist.append(r)
klist=list(set(klist))
klist.sort()

# solve
ans = 0
a=0
for k in klist:
    if k in ldict.keys():
        a+=ldict[k]
    if a>1:
        ans=max(ans,a)
#    print("[{}] {} ".format(k,a))
    if k in rdict.keys():
        a-=rdict[k]

# answer
print("{}".format(ans))
