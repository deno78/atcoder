n=int(input())
alist=[]
for i in range(n):
    alist.append(int(input()))

adic={}
aset=list(set(alist))
aset.sort()

for i in range(len(aset)):
    key=aset[i]
    val=i
    adic[key]=val

for a in alist:
    print(adic[a])