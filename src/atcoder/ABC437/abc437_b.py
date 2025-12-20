h,w,n=map(int,input().split())

hw=[]
for i in range(h):
    hw.append(list(map(int,input().split())))

blist=[]
for i in range(n):
    blist.append(int(input()))

ans=0
for w in hw:
    wk=0
    for b in blist:
        if b in w:
            wk+=1
    ans=max(ans,wk)

print(ans)        
