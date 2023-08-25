m=int(input())
dlist=list(map(int,input().split()))

a=sum(dlist)//2

for i in range(m):
    d=dlist[i]
    if a-d>=0:
        a-=d
    else:
        print("{} {}".format(i+1,a+1))
        exit()