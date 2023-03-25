n=int(input())
days=[]
ddic={}
for i in range(n):
    a,b=map(int,input().split())
    a2=a+b
    days.append(a)
    days.append(a2)
    if a not in ddic.keys():
        ddic[a]=0
    ddic[a]+=1
    if a2 not in ddic.keys():
        ddic[a2]=0
    ddic[a2]-=1

days=list(set(days))
days.sort()


nlist=[0]*(n+1)

cnt=0
d1=0
for i in range(len(days)-1):
    d1=days[i]
    d2=days[i+1]
    cnt+=ddic[d1]
    c=d2-d1
    nlist[cnt]+=c
#    print("day:{}-{} : num:{} ans[{}]: {} (+{})".format(
#        d1,d2,cnt,ddic[d1],nlist[cnt],c))

nlist.pop(0)
slist= [str(n) for n in nlist]
print(" ".join(slist))