n,m=map(int,input().split())

s=[]
for i in range(n):
    s.append(list(input()))

ans=set()
for i in range(n-m+1):
    for j in range(n-m+1):
        wk=[]
        for k in range(m):
            for l in range(m):
                wk.append(s[i+k][j+l])
#        print("".join(wk))
        ans.add("".join(wk))

print(len(ans))