n=int(input())
alist=list(map(int,input().split()))

bmap={}
for i in range(2**n):
    bag=[]
    total=0
    for j in range(n):
        if ((i>>j)&1):
            bag.append(j+1)
            total=total+alist[j]
    key=total%200
    line=str(len(bag)) + " " + " ".join(list(map(str,bag)))
    if key not in bmap.keys():
        bmap[key]=[]
    if line not in bmap[key]:
        bmap[key].append(line)
        if len(bmap[key])>1:
            print("Yes")
            print(bmap[key][0])
            print(line)
            exit()
print("No")
