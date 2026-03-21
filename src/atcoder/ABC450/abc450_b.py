n=int(input())
clists=[]

for i in range(n-1):
    clist=list(map(int,input().split()))
    clists.append(clist)
#print(clists)
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            # print(i,j,k)
            c1=clists[i][k-i-1]
            c2a=clists[i][j-i-1]
            c2b=clists[j][k-j-1]
            if c1>c2a+c2b:
                print('Yes')
                exit()
print('No')