import sys
# TODO edit the code

# param
n = int(input())
a=list(map(int,input().split()))

# solve
b=0
c=1
while c+b <=n:
#    print("{} {}".format(a[c+b-1],c),file=sys.stderr)
    if a[c+b-1]==c:
        c+=1
    else:
        b+=1

# answer
if b>=n:
    print(-1)
else:
    print(b)
