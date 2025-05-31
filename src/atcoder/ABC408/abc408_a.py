n,s=map(int,input().split())
tlist=list(map(int,input().split()))

tlist.insert(0,0)
for i in range(n):
    t1=tlist[i]
    t2=tlist[i+1]
    if t2-t1>=s+0.5:
        print("No")
        exit()

print("Yes")