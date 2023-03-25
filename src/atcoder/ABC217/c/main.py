n=int(input())
plist=list(map(int,input().split()))

pdic={}
for i in range(n):
    p=plist[i]-1
    pdic[p]=str(i+1)

qlist=[]
for i in range(n):
    qlist.append(pdic[i])
print(" ".join(qlist))