n=int(input())
xlist=list(map(int,input().split()))
xlist2=sorted(xlist)

m1=xlist2[n//2-1]
m2=xlist2[n//2]
#print("m={}[{}] or {}[{}]".format(m1,n//2,m2,n//2+1))
n2=n//2
for i in range(n):
    x=xlist[i]
    if x>=m2:
        print(m1)
    elif x<=m1:
        print(m2)
