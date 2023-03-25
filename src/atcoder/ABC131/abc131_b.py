n,l=map(int,input().split())
alist=range(l,n+l)
all=sum(alist)
ans=-1
diff=float('INF')
for a in alist:
    if abs(a) <= diff:
#        print("[{}] {}/{}".format(a,all-a,all))
        ans=all-a
        diff=abs(a)
print(ans)