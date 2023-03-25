n=int(input())

slist=list(map(int,input().split()))
tlist=list(map(int,input().split()))

ans=tlist
for i in range(n):
    s=slist[i]
    t=tlist[i]
    t2=t
    for j in range(n):
        i1=(i+j)%n
        i2=(i+j+1)%n
        t2=t2+slist[i1]
        if ans[i2] > t2:
            ans[i2]=t2
        else:
            break

for a in ans:
    print(a)
