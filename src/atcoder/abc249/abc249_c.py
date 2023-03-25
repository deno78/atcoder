# TODO edit the code

# param
n,k=map(int,input().split())
slist=[]
for i in range(n):
    slist.append(input())


# solve
ans=0
for i in range(2 ** n):
    bag = []
    p={}
    for j in range(n):
        if ((i >> j) & 1):
            bag.append(slist[j])
            for c in slist[j]:
                if c not in p.keys():
                    p[c]=0
                p[c]+=1
        wk=0
        for v in p.values():
            if v==k:
                wk+=1
        ans=max(wk,ans)
            

# answer
print(ans)
