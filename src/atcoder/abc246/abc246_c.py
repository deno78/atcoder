# TODO edit the code

# param
n,k,x=map(int,input().split())
alist=list(map(int,input().split()))

# solve
ans = sum(alist)
c=0
d=[]
for a in alist:
    c+=(a//x)
    d.append(a%x)
d.sort(reverse=True)
c2=k-c
d2=0
for i in range(min(k-c,len(d))):
    d2+=d[i]
# answer
print(ans- x*(min(k,c))-d2)
