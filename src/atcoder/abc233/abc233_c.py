def calc(lv,p):
    if lv==n:
        if p==x:
            return 1
        else:
            return 0
    else:
        ret=0
        for a in alist[lv]:
            ret+=calc(lv+1,p*a)
#            print("[{}]:{} * {}={} result:{}".format(lv,a,p,p*a,ret))
        return ret

n,x=map(int,input().split())

alist=[]
for i in range(n):
    alist.append(list(map(int,input().split()))[1:])
ans=calc(0,1)
print(ans)