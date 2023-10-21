# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
td=[]
tlist=[]
tdict1={}
tdict2={}
for i in range(n):
    t,d = map(int, input().split())
    t2=t+d
    td.append([t,d])
    tlist.append(t)
    tlist.append(t2)
    if t not in tdict1.keys():
        tdict1[t]=0
    tdict1[t]+=1
    if t2 not in tdict2.keys():
        tdict2[t2]=0
    tdict2[t2]+=1

tlist=list(set(tlist))
tlist.sort()

# solve
x=0
tdict={}
for t in tlist:
    if t in tdict1.keys():
        x+=tdict1[t]
    if t in tdict2.keys():
        x-=tdict2[t]
    tdict[t]=x
ans=0
for i in range(len(tlist)-1):
    t1=tlist[i]
    t2=tlist[i+1]
    print("{}-{} {}-{}".format(t1,t2,tdict[t1],tdict[t2]))
    if tdict[t1]>0 and tdict[t2]>0:
        ans+=min(t2-t1,tdict[t1],tdict[t2])
    # else:
    #     if tdict[t1]>0:
    #         ans+=1
    #     elif tdict[t2]>0:
    #         ans+=1

# answer
print(ans)
