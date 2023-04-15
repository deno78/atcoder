# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

def check(a,b):
    for i in range(len(a)):        
        for j in range(len(a)):
            if a[i][j]==1:
                if a[i][j]!=b[i][j]:
                    return False
    return True

# param
n = int(input())
amap=[]
for i in range(n):
    alist=list(map(int,input().split()))
    amap.append(alist)
bmap=[]
for i in range(n):
    blist=list(map(int,input().split()))
    bmap.append(blist)

bmap2=[]
bmap3=[]
bmap4=[]

for i in range(n):
    bmap2.append([0]*n)
    bmap3.append([0]*n)
    bmap4.append([0]*n)

# solve

for i in range(n):
    for j in range(n):
        bmap2[i][j]=bmap[n-j-1][i]
for i in range(n):
    for j in range(n):
        bmap3[i][j]=bmap2[n-j-1][i]
for i in range(n):
    for j in range(n):
        bmap4[i][j]=bmap3[n-j-1][i]

# for b in [bmap,bmap2,bmap3,bmap4]:
#     for i in range(len(b)):
#         print(b[i])
#     print("-----")

if check(amap,bmap):
    print("Yes")
    exit()
if check(amap,bmap2):
    print("Yes")
    exit()
if check(amap,bmap3):
    print("Yes")
    exit()
if check(amap,bmap4):
    print("Yes")
    exit()
print("No")