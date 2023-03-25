def mex(l):
    for i in range(max(l)+2):
        if i not in l:
            return i

nm = input().split()
n=int(nm[0])
m=int(nm[1])

alist = list(map(int,input().split()))

ans=99999999

for i in range(n-m+1):
    s=i
    e=i+m
    alist2 = alist[s:e]
    ans=min(mex(alist2),ans)
    if ans==0:
        break
print(ans)