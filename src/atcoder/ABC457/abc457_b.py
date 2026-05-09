n=int(input())
alist=[]
for i in range(n):
    alist.append(list(map(int,input().split())))

x,y=map(int,input().split())

print(alist[x-1][y])