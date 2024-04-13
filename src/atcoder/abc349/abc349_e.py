# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
amap=[]
for i in range(3):
    amap.append(list(map(int,input().split())))
bmap=[]
for i in range(3):
    bmap.append([0]*3)

vdict={}
for i in range(3):
    for j in range(3):
        if i!=1 and j!=1:
            a=amap[i][j]
            if a not in vdict.keys():
                vdict[a]=[]
            vdict[a].append([i,j])

t=0
a=0

while True:
    for i in range(3):
        if  [bmap[i][0],bmap[i][1],bmap[i][2]].count(1)==2:
            
        
