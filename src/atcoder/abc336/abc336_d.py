# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def check(l):
    ok=True
    for i in range(len(l)//2):
        i1=i+1
        i2=-1*(i+1)
#        print("\t{} [{}] {}:{} {}:{}".format(l,i1,i,l[i-1],i2,l[i2]))
        if l[i]<i1 or l[i2]<i1:
#            print("{} is false".format(l))
            ok=False
            break
    return ok


# param
n = int(input())
alist = list(map(int, input().split()))

# solve

ans=0
for i in range(n):
    sz=min(alist[i],n-i,i+1)
#    print("## Center:{} val:{} -> sz:{}".format(i,alist[i],sz))
    ok=0
    ng=sz+1
    t=0
    while ng-ok>1:
        m=(ok+ng)//2
        l=m-m+1
        r=m+m
        if check(alist[l:r]):
#            print("\t{}/{} {} ({}..{}) ={}".format(m,sz,alist[l:r],l,r,t))
            ok=m
            t=m
        else:
            ng=m

    ans=max(ans,t)

# answer
print(ans)
