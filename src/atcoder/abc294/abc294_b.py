h,w=map(int,input().split())


x=ord("A")-1
hw=[]
for i in range(h):
    alist=list(map(int,input().split()))
    hw.append(alist)

for i in range(h):
    alist=hw[i]
    ans=[]
    for a in alist:
        if a==0:
            ans.append(".")
        else:
            ans.append(chr(x+a))
    print("".join(ans))
