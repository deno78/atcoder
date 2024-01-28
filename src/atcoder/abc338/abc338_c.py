# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def max_a():
    ret=float("INF")
    for i in range(n):
        q=qlist[i]
        a=alist[i]
        if a>0:
            ret=min(ret,q//a)
    return ret

def chk(x):
    ret=float("INF")
    for i in range(n):
        q=qlist[i]
        a=alist[i]
        b=blist[i]
        if b>0:
            ret=min(ret,(q-(a*x))//b )
    return ret

def ok(xlist,ylist,zlist,a,b):
    for i in range(len(xlist)):
        if ylist[i]*a+zlist[i]*b>xlist[i]:
            return False
    return True


# param
n = int(input())
qlist=list(map(int,input().split()))
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))

ans=0
x=max_a()
for i in range(x+1):
    b=chk(i)
    ans=max(ans,i+b)

# solve

print(ans)
