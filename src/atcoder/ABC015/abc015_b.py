import math
n=int(input())
alist=list(map(int,input().split()))
c=0
x=0
for a in alist:
    if a>0:
        c+=1
        x+=a

print(int(math.ceil(x/c)))