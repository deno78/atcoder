n,m,x=map(int,input().split())

alist=list(map(int,input().split()))

alist.sort()

a1=0
a2=0
for a in alist:
    if a>x:
        a1+=1
    elif a<x:
        a2+=1

print(min(a1,a2))