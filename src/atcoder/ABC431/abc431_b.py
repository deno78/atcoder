x=int(input())
n=int(input())
wlist=list(map(int,input().split()))
q=int(input())
plist=[]
for i in range(q):
    plist.append(int(input()))

plist2=[0]*(len(wlist))
for i in range(q):
    p=plist[i]
    w2=wlist[p-1]
    if plist2[p-1]==0:
        plist2[p-1]=1
        x+=w2
    else:
        plist2[p-1]=0
        x-=w2
    print(x)
