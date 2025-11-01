from bisect import bisect,bisect_right,bisect_left
n,a,b=map(int,input().split())
s=input()

alist=[]
blist=[]
x=0
y=0
alist.append(x)
blist.append(y)
for i in range(n):
    if s[i]=="a":
        x+=1
    elif s[i]=="b":
        y+=1
    alist.append(x)
    blist.append(y)

ans=0
for l in range(n):
    a1=alist[l]
    b1=blist[l]
    i1=bisect_left(alist,a+a1)
    i2=bisect_left(blist,b+b1)
#    print(l+1,i1,i2-1,i2-i1)
    ans+=(max(0,i2-i1))

print(ans)
