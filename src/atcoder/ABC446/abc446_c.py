T=int(input())
for _ in range(T):
    n,d=map(int,input().split())
    alist=list(map(int,input().split()))
    blist=list(map(int,input().split()))
    stock=[0]*n
    pos=0
    all=0
    for i in range(n):
        stock[i]=alist[i]
        all+=alist[i]
        b=blist[i]
        dead=0
        for j in range(pos,i+1):
            if b==0:
                break
            if stock[j]>b:
                stock[j]-=b
                all-=b
                b=0
            else:
                b-=stock[j]
                all-=stock[j]
                stock[j]=0
                pos=j+1
        if i>=d:
            dead=stock[i-d]
            stock[i-d]=0
            pos=max(pos,i-d)
            all-=dead
#            print(i,"dead:",dead)
#        print(i,alist[i],blist[i],pos,stock,all)
    print(all)


