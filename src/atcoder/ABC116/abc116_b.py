def func(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

s=int(input())

aset=set()
aset.add(s)
cnt=0
while True:
    cnt=cnt+1
    s2=func(s)
    print("{} -> {}".format(s,s2))
    if s2 in aset:
        print(cnt+1)
        exit()
    else:
        s=s2
        aset.add(s2)
