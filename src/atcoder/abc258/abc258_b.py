# TODO edit the code

def get_around(x,y,hist):
    ret={}
    for i in range(9):
        xd=i%3-1
        yd=i//3-1
        if xd!=0 and yd!=0:
            x2=(x+xd)%n
            y2=(y+yd)%n
            if [x2,y2] not in hist:
                a2=alist[x2][y2]
                if a2 not in ret.keys():
                    ret[a2]=[]
                ret[a2].append([x2,y2])
    return ret[max(ret.keys())]

# param
n = int(input())
alist=[]
for i in range(n):
    alist.append(list(map(int,list(input()))))

s=-1
for a in alist:
    s=max(s,max(a))

# solve
wk=[]
for i in range(n):
    for j in range(n):
        if alist[i][j]==s:
            wk.append([i,j,[s],[[i,j]]])
ans=-1
while len(wk) > 0:
    a = wk.pop()
    print(a)
    if len(a[3])==n:
        ans = max(ans,int("".join(a[2])))
    else:
        for w in get_around(a[0],a[1],a[3]):
            x2=w[0]
            y2=w[1]
            h2=a[3].append([w[0],w[1]])
            a2=alist[x2][y2]
            print(a2)
            ary2=a[2].append(a2)
            wk.append([x2,y2,ary2,h2])

# answer
print(ans)
