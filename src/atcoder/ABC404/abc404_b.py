n=int(input())

s=[]
for i in range(n):
    s.append(list(input()))
t=[]
for i in range(n):
    t.append(list(input()))

t2=[]
for i in range(n):
    wk=[]
    for j in range(n):
        wk.append(t[n-j-1][i])
    t2.append(wk)
t3=[]
for i in range(n):
    wk=[]
    for j in range(n):
        wk.append(t2[n-j-1][i])
    t3.append(wk)
t4=[]
for i in range(n):
    wk=[]
    for j in range(n):
        wk.append(t3[n-j-1][i])
    t4.append(wk)


ans=float("INF")
wk=0
for i in range(n):
    for j in range(n):
        if s[i][j]!=t[i][j]:
            wk+=1
ans=min(ans,wk)
wk=3
for i in range(n):
    for j in range(n):
        if s[i][j]!=t2[i][j]:
            wk+=1
ans=min(ans,wk)
wk=2
for i in range(n):
    for j in range(n):
        if s[i][j]!=t3[i][j]:
            wk+=1
ans=min(ans,wk)
wk=1
for i in range(n):
    for j in range(n):
        if s[i][j]!=t4[i][j]:
            wk+=1
ans=min(ans,wk)

print(ans)