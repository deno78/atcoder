# TODO edit the code

# param
n = int(input())

ans=[]

# solve
for i in range(n):
    ans.append([])
    for j in range(i+1):
        if j==0 or j==i:
            ans[i].append(str(1))
        else:
            ans[i].append(str(int(ans[i-1][j-1]) + int(ans[i-1][j])))

for a in ans:
    print(" ".join(a))