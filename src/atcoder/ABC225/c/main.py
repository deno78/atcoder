n,m=map(int,input().split())

b=[]
for i in range(n):
    b.append(list(map(int,input().split())))

#print("{}/{}".format((b[0][0]-1)%7,(7-m)))
if (b[0][0]-1)%7 > (7-m):
    print('No')
    exit()

for j in range(m-1):
    if b[n-1][j]+1!=b[n-1][j+1]:
        print('No')
        exit()

for i in range(n-1):
    if b[i][0]+7 != b[i+1][0]:
        print('No')
        exit()
    for j in range(m-1):
        if b[i][j]+1!=b[i][j+1]:
            print('No')
            exit()

print('Yes')