alist=[]
for i in range(3):
    alist.append(list(map(int,input().split())))

ans=0
for i in range(6):
    for j in range(6):
        for k in range(6):
            wk=[alist[0][i], alist[1][j], alist[2][k]]
            wk.sort()
            if wk[0]==4 and wk[1]==5 and wk[2]==6:
                ans+=1

print(ans/(6**3))