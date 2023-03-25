n,k=map(int,input().split())

alist=list(map(int,input().split()))
alist2=sorted(alist)
# 全国民に配れるだけ配る
b=k//n
k-=b*n

m=alist2[k-1]

#print("k:{} m:{}".format(k,m))
for i in range(n):
    a=alist[i]
    if a <= m and k>0:
        print(b+1)
    else:
        print(b)

