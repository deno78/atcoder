# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n,m = map(int,input().split())
ab=[]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    ab.append([a,b])

# solve
ans = 0
s={}

ans=n*n
for a,b in ab:
    if a not in s:
        s[a]={}
    if b not in s[a]:
        s[a][b]=""
    if s[a][b]!="#":
        ans-=1
    s[a][b]="#"
    for dx,dy in [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]:
        x=a+dx
        y=b+dy
        if 0<=x and x<n and 0<=y and y<n:
            if x not in s:
                s[x]={}
            if y not in s[x]:
                s[x][y]=""
            if s[x][y]!="#":
                s[x][y]="#"
                ans-=1

# answer
print("{}".format(ans))
