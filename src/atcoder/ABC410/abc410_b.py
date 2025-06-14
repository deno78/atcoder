n,q=map(int,input().split())
xlist=list(map(int, input().split()))

box=[0]*n
ans=[-1]*q

for i in range(q):
    x=xlist[i]
    if x==0:
        m=min(box)
        for j in range(n):
            if box[j]==m:
                ans[i]=j+1
                box[j]+=1
                break
    else:
        box[x-1]+=1
        ans[i]=x

ans2=[]
for a in ans:
    ans2.append(str(a))

print(" ".join(ans2))
