n = int(input(''))
alist = list(map(int,input('').split()))

alist.sort()
p=alist[0]

ans=0
cnt=0
p=alist[0]
for a in alist:
#    print("{}/{}".format(a,p))
    if a==p:
        cnt+=1
    else:
#        print("\t[{} / {}] -> {}".format(p,cnt,ans))
        if cnt > p:
            ans+=(cnt-p)
        elif cnt < p:
            ans+=cnt
        cnt=1
        p=a

if cnt > p:
    ans+=(cnt-p)
elif cnt < p:
    ans+=cnt

print(ans)
