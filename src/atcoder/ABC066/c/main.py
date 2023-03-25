n=int(input())
alist=list(map(int,input().split()))

blist1=[]
blist2=[]
for i in range(n):
    if i%2==0:
        blist1.append(str(alist[i]))
    else:
        blist2.append(str(alist[i]))

if n%2==0:
    print(" ".join(reversed(blist2)) + " " + " ".join(blist1))
else:
    print(" ".join(reversed(blist1)) + " " + " ".join(blist2))
