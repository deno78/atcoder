t=int(input())
tlist=[]
ans=[]
for i in range(t):
    n=int(input())
    alist=list(map(int,input().split()))
    x=0
    for a in alist:
        if a%2==1:
            x+=1
    ans.append(x)
for a in ans:
    print(a)

