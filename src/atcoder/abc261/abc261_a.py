# TODO edit the code

# param
l1,r1,l2,r2=map(int,input().split())

if r1 < l2  or r2 < l1:
    print(0)
    exit()
else:
    l=max(l1,l2)
    r=min(r1,r2)
    print(r-l)
