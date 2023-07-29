# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

adict={}
bdict={}
adict[max(alist)+1]=0
bdict[max(blist)+1]=0

for a in alist:
    if a not in adict.keys():
        adict[a]=0
    adict[a]+=1
for b in blist:
    b+=1
    if b not in bdict.keys():
        bdict[b]=0
    bdict[b]+=1

keys=[]
keys.extend(adict.keys())
keys.extend(bdict.keys())
keys=list(set(keys))
keys.sort()
xa=0
xb=len(blist)
for key in keys:
    wa=0
    wb=0
    if key in adict.keys():
        wa=adict[key]
    if key in bdict.keys():
        wb=bdict[key]
    xa+=wa
    xb-=wb
#    print("[{}] {}/{}".format(key,xa,xb))
    if xa>=xb:
        print(key)
        exit()
