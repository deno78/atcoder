n=int(input())

s=[]
for i in range(n):
    s.append(list(input()))

ans=[]
for i in range(n):
    ans.append([""]*n)

for i in range(n):
    for j in range(n):
        ans[i][j]=s[n-j-1][i]

for i in range(n):
    print("".join(ans[i]))