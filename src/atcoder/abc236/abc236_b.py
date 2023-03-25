# TODO edit the code

# param
n = int(input())
alist=list(map(int,input().split()))

nlist=[0]*(n+1)
# solve
for a in alist:
    nlist[a]+=1    



# answer
print(nlist.index(3))
