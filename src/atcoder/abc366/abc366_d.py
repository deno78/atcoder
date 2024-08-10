# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        alist=list(map(int,input().split()))
        a[i].append(alist)

q=int(input())
qlist=[]
for i in range(q):
    qlist.append(list(map(int,input().split())))

# solve
a2=[]
for i in range(n):
    a2.append([])
    for j in range(n):
        a2[i].append([0]*n)
print(a)
a2[0][0][0]=a[0][0][0]
for i in range(n):
    for j in range(n):
        for k in range(n):
            x0=a[i][j][k]
            x1=0
            x2=0
            x3=0
            x6=0
            x7=0
            x8=0
            x9=0
            if i>0:
                x1=a2[i-1][j][k]
            if j>0:
                x2=a2[i][j-1][k]
            if k>0:
                x3=a2[i][j][k-1]
            if i>0 and j>0:
                x6=a2[i-1][j-1][k]
            if j>0 and k>0:
                x7=a2[i][j-1][k-1]
            if i>0 and k>0:
                x8=a2[i-1][j][k-1]
            if i>0 and j>0 and k>0:
                x9=a2[i-1][j-1][k-1]
            a2[i][j][k]=x0+x1+x2+x3-x6-x7-x8+x9
            print("{} {} {}=> {} {} {} {} =>{}".format(i,j,k,x0,x1,x2,x3,a2))


print(a2)
# answer
for i in range(q):
    lx,rx,ly,ry,lz,rz=qlist[i]
    lx-=1
    rx-=1
    ly-=1
    ry-=1
    lz-=1
    rz-=1
    x1=a2[lz][ly][lx]
    x2=a2[rz][ry][rx]
    print("{}-{}-{}  {}-{}-{}".format(lz,ly,lx,rz,ry,rx))
    print("{}-{}".format(x2,x1))
    print("{}".format(x2-x1))
    