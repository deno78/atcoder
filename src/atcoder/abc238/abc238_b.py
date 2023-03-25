# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))

# solve
blist=[]
blist.append(0)
t=0
for i in range(n):
    a=alist[i]
    t=(a+t)%360
    blist.append(t)

blist=sorted(list(set(blist)))
blist.append(360)
ans = 0
b1=blist[0]
for b in blist:
    b2=b-b1
    ans=max(ans,b2)
    b1=b


# answer
print(ans)
