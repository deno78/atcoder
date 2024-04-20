# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int, input().split())
ab={}
for i in range(n):
    ab[i]=[]

abmap=[]
for i in range(n):
    abmap.append([0]*n)

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    ab[a].append(b)
    ab[b].append(a)
    abmap[a][b]=1
    abmap[b][a]=1

# solve
ans=0
for x in range(n-1):
    for z in range(x+1,n):
        if abmap[x][z]==0:
            for y in ab[x]:
                if y!=z and abmap[y][z]==1:
#                    print("{} ({}) {} ({}) {} ->{}".format(x,abmap[x][y],y,abmap[y][z],z,abmap[z][x]))
                    abmap[x][z]=1
                    abmap[z][x]=1
                    ab[x].append(z)
                    ab[z].append(x)
                    ans+=1
                    break
#                    print("{} {} {}".format(x+1,y+1,z+1))

# answer
print("{}".format(ans))
