# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
h,w,q = map(int, input().split())
rc=[]
for i in range(q):
    r,c=map(int,input().split())
    r-=1
    c-=1
    rc.append([r,c])

m=[]
for i in range(h):
    m.append([1]*w)

# solve
direction=[[-1,0],[1,0],[0,-1],[0,1]]
ans=0
for i in range(q):
    r,c=rc[i]
    dflag=[0]*4
    for j in range(max(h,w)):
        for k in range(4):
            if dflag[k]==0:
                d=direction[k]
                nr=r+d[0]*j
                nc=c+d[1]*j
                if 0>nr or nr>=h or 0>nc or nc>=w:
                    dflag[k]=1
                elif m[nr][nc]==1:
                    m[nr][nc]=0
                    ans+=1
                    dflag[k]=1
        if dflag.count(0)==0:
            break
    # print("[{}] {},{}".format(i,r,c))
    # for x in m:
    #     print(x)

# answer
print(h*w-ans)