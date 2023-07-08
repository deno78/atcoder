# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())
amap=[]
for i in range(n):
    amap.append(list(input()))

# solve
ans = []
for i in range(n):
    ans.append([" "]*(n))

for i in range(n):
    for j in range(n):
        if i!=0 and i!=n-1 and j!=0 and j!=n-1:
            ans[i][j]=amap[i][j]
        else:
            if i==0 and j==0:
                ans[i][j]=amap[i+1][j]
            elif i==0 and j==n-1:
                ans[i][j]=amap[i][j-1]
            elif i==n-1 and j==n-1:
                ans[i][j]=amap[i-1][j]
            elif i==n-1 and j==0:
                ans[i][j]=amap[i][j+1]
            elif i==0:
                ans[i][j]=amap[i][j-1]
            elif i==n-1:
                ans[i][j]=amap[i][j+1]
            elif j==0:
                ans[i][j]=amap[i+1][j]
            elif j==n-1:
                ans[i][j]=amap[i-1][j]


            

# answer
for i in range(n):
    print("".join(ans[i]))
