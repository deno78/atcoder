n=int(input())
alist=list(map(int,input().split()))

clist=list(set(alist))
clist.sort()
clist2=[]
for c in clist:
    clist2.append(str(c))
print(len(clist2))
print(" ".join(clist2))