h,w=map(int,input().split())

c=[]
for i in range(h):
    c.append(list(input()))

for i in range(h):
    for j in range(w):
        if c[i][j] == '#':
            ok = False
            ds=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            for d in ds:
                x=d[0]
                y=d[1]
                if x>=0 and y>=0 and x<h and y<w and c[x][y]=='#':
                    ok = True
            if not ok:
                print("No")
                exit()
print("Yes")
                
                