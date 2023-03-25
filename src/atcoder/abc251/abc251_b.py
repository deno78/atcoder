# TODO edit the code
import itertools

# param
n,w=map(int,input().split())

alist=list(map(int,input().split()))
alist.append(0)

# solve
ans=[]
for a in alist:
    if a<=w and a>0:
        ans.append(a)
for c in itertools.combinations(alist,3):
    s=sum(c)
    if s<=w and s>0:
        ans.append(sum(c))

# answer
print(len(set(ans)))
