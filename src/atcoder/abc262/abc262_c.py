n=int(input())
alist=list(map(int,input().split()))

eqlist=[]
neqdic={}
for i in range(n):
    a=alist[i]
    if a==(i+1):
        eqlist.append(i)
    else:
        if a not in neqdic.keys():
            neqdic[a]=[]
        neqdic[a].append(i)

ans=0
# Case: i=min,j=max
for i in range(len(eqlist)-1):
    for j in range(i+1,len(eqlist)):
#        print("a[{}] [{}]".format(eqlist[i],eqlist[j]))
        ans+=1

# Case: i=min,j=max
for a1,ilist in neqdic.items():
    for i in ilist:
        if (i+1) in neqdic.keys():
            jlist=neqdic[i+1]
            if (a1-1) in jlist and (a1-1)>i:
                ans+=1
#                print("a1:{} i:{} jlist:{}".format(a1,i,jlist))

print(ans)
