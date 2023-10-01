# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,q = map(int, input().split())
s = list(map(int,list(input())))
qlist=[]
for i in range(q):
    qlist.append(list(map(int,input().split())))

# solve

for i in range(q):
    c,l,r=qlist[i]
    if c==1:
        for j in range(l,r):
            s[j]=~s[j] &1
    elif c==2:
        ans=0
        x=0
        y=0
        while y<(r-l):
            if s[x]==0:
                x=s.index(1,x+1)
                y=x+1
            elif s[y]==1:
                y+=1
                ans=max(ans,y-x)
            print("{}-{} {}".format(x,y,s[x:y]))
        print(ans)