import itertools
# TODO edit the code

def calc(blist):
    result=0
    for i in range(n):
        b1=min([blist[2*i],blist[2*i+1]])
        b2=max([blist[2*i],blist[2*i+1]])
        result^= alist[b1][b2-b1-1]
    return result

# param
n = int(input())
alist=[]
for i in range(2*n-1):
    alist.append(list(map(int,input().split())))

ans = 0

cache=[]

for l in list(itertools.permutations(range(2*n))):
    c=[]
    for i in range(n):
        b1=min([l[2*i],l[2*i+1]])
        b2=max([l[2*i],l[2*i+1]])
        c.append("{}-{}".format(b1,b2))
    if c not in cache:
        ans=max(ans,calc(l))
        cache.append(c)

# solve

# answer
print(ans)
