# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,t = map(int, input().split())
ab=[]
for i in range(t):
    a,b=map(int,input().split())
    ab.append([a,b])
xdict={}
ydict={}
for i in range(1,n+1):
    xdict[i]=0
ydict[0]=n
for i in range(t):
    a,b=ab[i]
    b1=xdict[a]
    xdict[a]+=b
    b2=xdict[a]
    ydict[b1]-=1
    if ydict[b1]==0:
        ydict.pop(b1)
    if b2 not in ydict.keys():
        ydict[b2]=0
    ydict[b2]+=1
    print(len(ydict.keys()))

# solve

# answer
