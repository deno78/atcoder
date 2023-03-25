# TODO edit this code

# param
n,m,t=map(int,input().split())
alist = list(map(int,input().split()))
xydic = {}
for i in range(m):
    x,y=map(int,input().split())
    xydic[x-1]=y

# solve
for i in range(n-1):
    a=alist[i]
    t-=a
    if i in xydic.keys():
        t+=xydic[i]
    if t<=0:
        print('No')
        exit()


# answer
print("Yes")
