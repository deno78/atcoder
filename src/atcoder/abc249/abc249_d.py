n = int(input())
alist=list(map(int,input().split()))

adic={}
for a in alist:
    if a not in adic.keys():
        adic[a]=0
    adic[a]+=1

# solve
ans=0
alist2=list(adic.keys())
alist2.sort()
ma=max(alist2)
for ai in alist2:
    for k in alist2:
        aj=ai*k
        if aj>ma:
            break
        else:
            if aj in adic.keys():
                ans+=adic[ai]*adic[aj]*adic[k]
#        print("{}/{}={} [{}]".format(aj,ai,k,ans))

# answer
print(ans)
