n,q=map(int,input().split())

ans=[]
for i in range(n):
    ans.append(["N"]*n)

for i in range(q):
    s=input().split()
    a=int(s[1])-1
    if s[0]=="1":
        b=int(s[2])-1
        ans[b][a]="Y"
    elif s[0]=="2":
        for j in range(n):
            if ans[a][j] =="Y":
                ans[j][a]="Y"
    elif s[0]=="3":
        for j in range(n):
            for k in range(n):
                if ans[a][j] == "Y" and ans[j][k]=="Y":
                    ans[k][a]="Y"

for l in ans:
    print("".join(l))
