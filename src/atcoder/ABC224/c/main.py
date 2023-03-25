n=int(input())
xy=[]
for i in range(n):
    xy.append(list(map(int,input().split())))

cnt=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a=xy[i]
            b=xy[j]
            c=xy[k]
            abx=(a[0]-b[0])
            acx=(a[0]-c[0])
            aby=(a[1]-b[1])
            acy=(a[1]-c[1])

            if abx==0 and acx==0:
                pass
            elif abx==0 or acx==0:
                cnt+=1
            else:
                d1=aby*acx
                d2=acy*abx
                if d1!=d2:
                    cnt+=1

print(cnt)