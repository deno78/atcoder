# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import sys

sys.setrecursionlimit(2000)

def search(val):
    ret=val
    for i in range(n):
        if used[i]==0:
            used[i]=1
            for j in range(n):
                if used[j]==0:
                    used[j]=1
#                    print("{}-{} value:{} used:{}".format(i,j,val+dmap[i][j],used))
                    wk=search(val+dmap[i][j])
                    if used.count(0)<2:
                        ret=max(ret,wk)
                    used[j]=0
            used[i]=0
    return ret


# param
n = int(input())
dmap=[]
vdict={}
for i in range(n):
    dmap.append([0]*(n))

for i in range(n-1):
    d=list(map(int,input().split()))
    for j in range(len(d)):
        x=i
        y=j+i+1
        dmap[x][y]=d[j]
        dmap[y][x]=d[j]

# solve
used=[0]*n

ans=search(0)
# answer
print("{}".format(ans))
