t,x=map(int,input().split())
alist=list(map(int,input().split()))

ans=[]
a1=alist[0]
ans.append([0,alist[0]])
for i in range(1,t+1):    
    a2=alist[i]
    if abs(a1-a2)>=x:
        ans.append([i,a2])
        a1=a2

for t,a in ans:
    print(t,a)